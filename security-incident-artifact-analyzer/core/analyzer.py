"""
analyzer.py

Entry point for running all artifact parsers and generating reports.
"""

import argparse
from typing import Dict, Any

from parsers.registry_parser import RegistryParser
from parsers.browser_history import BrowserHistoryParser
from parsers.sysmon_parser import SysmonParser
from parsers.network_parser import NetworkParser
from core.report import ReportGenerator


def aggregate_results(args: argparse.Namespace) -> Dict[str, Any]:
    """
    Initialize parsers and aggregate their results into a single structure.
    """

    results: Dict[str, Any] = {}

    if args.registry:
        registry_parser = RegistryParser(args.registry)
        results["registry"] = registry_parser.run()

    if args.browser:
        browser_parser = BrowserHistoryParser(args.browser)
        results["browser_history"] = browser_parser.run()

    if args.sysmon:
        sysmon_parser = SysmonParser(args.sysmon)
        results["sysmon"] = sysmon_parser.run()

    if args.network:
        network_parser = NetworkParser(args.network)
        results["network"] = network_parser.run()

    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Security Incident Artifact Analyzer - DFIR artifact analysis tool."
    )

    parser.add_argument(
        "--registry",
        help="Path to registry hive or exported registry file.",
    )
    parser.add_argument(
        "--browser",
        help="Path to browser profile directory or history SQLite DB.",
    )
    parser.add_argument(
        "--sysmon",
        help="Path to Sysmon log file (EVTX/CSV/etc.).",
    )
    parser.add_argument(
        "--network",
        help="Path to network logs or PCAP-derived data.",
    )
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Directory where reports will be written.",
    )
    parser.add_argument(
        "--no-markdown",
        action="store_true",
        help="Do not generate Markdown report.",
    )
    parser.add_argument(
        "--no-json",
        action="store_true",
        help="Do not generate JSON report.",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    aggregated = aggregate_results(args)

    if not aggregated:
        print("No input artifacts provided. Use --registry/--browser/--sysmon/--network.")
        return

    reporter = ReportGenerator(args.output_dir)

    if not args.no_json:
        json_path = reporter.to_json(aggregated)
        print(f"[+] JSON report written to: {json_path}")

    if not args.no_markdown:
        md_path = reporter.to_markdown(aggregated)
        print(f"[+] Markdown report written to: {md_path}")


if __name__ == "__main__":
    main()
