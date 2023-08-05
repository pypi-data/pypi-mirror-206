# -*- coding: utf-8 -*-

"""Query, download, and format Wikidata as a registry."""

import json
import logging
from textwrap import dedent
from typing import Dict

import click

from bioregistry.constants import BIOREGISTRY_PATH, EXTERNAL, URI_FORMAT_KEY
from bioregistry.utils import query_wikidata, removeprefix

__all__ = [
    "get_wikidata",
]

DIRECTORY = EXTERNAL / "wikidata"
DIRECTORY.mkdir(exist_ok=True, parents=True)
PROCESSED_PATH = DIRECTORY / "processed.json"

logger = logging.getLogger(__name__)

PROPERTIES_QUERY = dedent(
    """\
    SELECT ?propStr
    WHERE {
      VALUES ?category {
        wd:Q21294996  # chemistry
        wd:Q22988603  # biology
        wd:Q80840868  # research
      }
      ?prop wdt:P31/wdt:P279+ ?category .
      BIND( SUBSTR(STR(?prop), 32) AS ?propStr )
    }
    ORDER BY ?prop
    """
)

#: A query to wikidata for properties related to chemistry, biology, and related
QUERY_FMT = dedent(
    """\
    SELECT DISTINCT
      (?prop AS ?prefix)
      ?propLabel
      ?propDescription
      ?miriam
      ?pattern
      (GROUP_CONCAT(DISTINCT ?homepage_; separator='\\t') AS ?homepage)
      (GROUP_CONCAT(DISTINCT ?format_; separator='\\t') AS ?uri_format)
      (GROUP_CONCAT(DISTINCT ?format_rdf_; separator='\\t') AS ?uri_format_rdf)
      (GROUP_CONCAT(DISTINCT ?database_; separator='\\t') AS ?database)
      (GROUP_CONCAT(DISTINCT ?example_; separator='\\t') AS ?example)
      (GROUP_CONCAT(DISTINCT ?short_name_; separator='\\t') AS ?short_name)
    WHERE {
      {
        VALUES ?category {
          wd:Q21294996  # chemistry
          wd:Q22988603  # biology
          wd:Q80840868  # research
        }
        ?prop wdt:P31/wdt:P279+ ?category .
      }
      UNION {
        VALUES ?prop { %s }
      }
      BIND( SUBSTR(STR(?prop), 32) AS ?propStr )
      OPTIONAL { ?prop wdt:P1793 ?pattern }
      OPTIONAL { ?prop wdt:P4793 ?miriam }

      OPTIONAL { ?prop wdt:P1813 ?short_name_ }
      OPTIONAL { ?prop wdt:P1896 ?homepage_ }
      OPTIONAL { ?prop wdt:P1630 ?format_ }
      OPTIONAL { ?prop wdt:P1921 ?format_rdf_ }
      OPTIONAL { ?prop wdt:P1629 ?database_ }
      OPTIONAL {
        ?prop p:P1855 ?statement .
        ?statement ?propQualifier ?example_ .
        FILTER (STRSTARTS(STR(?propQualifier), "http://www.wikidata.org/prop/qualifier/"))
        FILTER (?propStr = SUBSTR(STR(?propQualifier), 40))
      }
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    }
    GROUP BY ?prop ?propLabel ?propDescription ?miriam ?pattern
    ORDER BY ?prop
    """
)

RENAMES = {"propLabel": "name", "propDescription": "description"}
CANONICAL_DATABASES = {
    "P6800": "Q87630124",  # -> NCBI Genome
    "P627": "Q48268",  # -> International Union for Conservation of Nature
    "P351": "Q1345229",  # NCBI Gene
    "P4168": "Q112783946",  # Immune epitope database
}

CANONICAL_HOMEPAGES: Dict[str, str] = {
    "P6852": "https://www.ccdc.cam.ac.uk",
    "P7224": "http://insecta.pro/catalog",
}
CANONICAL_URI_FORMATS = {
    "P830": "https://eol.org/pages/$1",
    "P2085": "https://jglobal.jst.go.jp/en/redirect?Nikkaji_No=$1",
    "P604": "https://medlineplus.gov/ency/article/$1.htm",
    "P492": "https://omim.org/OMIM:$1",
    "P486": "http://www.nlm.nih.gov",
    "P3201": "http://bioportal.bioontology.org/ontologies/MEDDRA?p=classes&conceptid=$1",
    "P7224": "http://insecta.pro/taxonomy/$1",
    "P3088": "https://taibnet.sinica.edu.tw/eng/taibnet_species_detail.php?name_code=$1",
    "P8150": "https://search.bvsalud.org/global-literature-on-novel-coronavirus-2019-ncov/resource/en/$1",
    "P9272": "https://decs.bvsalud.org/ths/resource/?id=$1",
    "P8082": "https://www.mscbs.gob.es/ciudadanos/centros.do?metodo=realizarDetalle&tipo=hospital&numero=$1",
    "P10095": "https://www.surgeons.org/Profile/$1",
    "P5397": "http://www.tierstimmen.org/en/database?field_spec_species_target_id_selective=$1",
}

# Stuff with miriam IDs that shouldn't
MIRIAM_BLACKLIST = {
    "Q51162088",
    "Q56221155",
    "Q47519952",
    "Q106201514",
    "Q106201090",
    "Q106201991",
    "Q106201090",
    "Q106201514",
    "Q106201904",
    "Q106201991",
    "Q106832467",
    "Q96212863",
    "Q106695243",
    "Q51162088",
    "Q56221155",
    "Q47519952",
}


def _get_mapped():
    return {
        value
        for record in json.loads(BIOREGISTRY_PATH.read_text()).values()
        for metaprefix, value in record.get("mappings", {}).items()
        if metaprefix == "wikidata"
    }


def _get_query(properties) -> str:
    values = " ".join(f"wd:{p}" for p in properties)
    return QUERY_FMT % values


def _get_wikidata():
    """Iterate over Wikidata properties connected to biological databases."""
    mapped = _get_mapped()
    # throw out anyhting that can be queried directly
    mapped.difference_update(
        bindings["propStr"]["value"]
        for bindings in query_wikidata(PROPERTIES_QUERY)
        if bindings["propStr"]["value"].startswith("P")  # throw away any regular ones
    )
    rv = {}
    for bindings in query_wikidata(_get_query(mapped)):
        examples = bindings.get("example", {}).get("value", "").split("\t")
        if examples and all(
            example.startswith("http://www.wikidata.org/entity/") for example in examples
        ):
            # This is a relationship
            continue

        bindings = {
            RENAMES.get(key, key): value["value"]
            for key, value in bindings.items()
            if value["value"]
        }

        prefix = bindings["prefix"] = removeprefix(
            bindings["prefix"], "http://www.wikidata.org/entity/"
        )
        for key in [
            "homepage",
            "uri_format_rdf",
            URI_FORMAT_KEY,
            "database",
            "example",
            "short_name",
        ]:
            if key in bindings:
                bindings[key] = tuple(
                    sorted(
                        removeprefix(value, "http://www.wikidata.org/entity/")
                        for value in bindings[key].split("\t")
                    )
                )

        for key, canonicals in [
            ("database", CANONICAL_DATABASES),
            ("homepage", CANONICAL_HOMEPAGES),
            ("uri_format", CANONICAL_URI_FORMATS),
        ]:
            # sort by increasing length - the assumption being that the shortest
            # one has the least amount of nonsense, like language tags or extra
            # parameters
            values = sorted(bindings.get(key, []), key=len)
            if not values:
                pass
            elif len(values) == 1:
                bindings[key] = values[0]
            elif prefix not in canonicals:
                logger.warning(
                    "[wikidata] need to curate canonical %s for %s (%s):",
                    key,
                    prefix,
                    bindings["name"],
                )
                for value in values:
                    logger.warning("  %s", value)
                bindings[key] = values[0]
            else:
                bindings[key] = canonicals[prefix]

        pattern = bindings.get("pattern")
        if pattern:
            if not pattern.startswith("^"):
                pattern = "^" + pattern
            if not pattern.endswith("$"):
                pattern = pattern + "$"
            bindings["pattern"] = pattern

        rv[prefix] = bindings

    return rv


def get_wikidata(force_download: bool = False):
    """Get the wikidata registry."""
    if PROCESSED_PATH.exists() and not force_download:
        with PROCESSED_PATH.open() as file:
            return json.load(file)

    data = _get_wikidata()
    with PROCESSED_PATH.open("w") as file:
        json.dump(data, file, indent=2, sort_keys=True)
    return data


@click.command()
def _main():
    data = get_wikidata(force_download=True)
    click.echo(f"Got {len(data):,} records")


if __name__ == "__main__":
    _main()
