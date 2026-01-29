"""Unified CLI registry - single source of truth for CLI metadata."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CLIInfo:
    """Metadata for a supported AI CLI."""

    name: str
    display_name: str
    adapter_module: str


CLI_REGISTRY: dict[str, CLIInfo] = {
    "claude": CLIInfo(
        name="claude",
        display_name="Claude Code",
        adapter_module="ai_comm.adapters.claude",
    ),
    "codex": CLIInfo(
        name="codex",
        display_name="Codex CLI",
        adapter_module="ai_comm.adapters.codex",
    ),
    "gemini": CLIInfo(
        name="gemini",
        display_name="Gemini CLI",
        adapter_module="ai_comm.adapters.gemini",
    ),
    "aider": CLIInfo(
        name="aider",
        display_name="Aider",
        adapter_module="ai_comm.adapters.aider",
    ),
    "cursor": CLIInfo(
        name="cursor",
        display_name="Cursor",
        adapter_module="ai_comm.adapters.cursor",
    ),
    "opencode": CLIInfo(
        name="opencode",
        display_name="OpenCode",
        adapter_module="ai_comm.adapters.opencode",
    ),
}


def get_display_name(cli_name: str) -> str:
    """Get human-readable display name for CLI."""
    info = CLI_REGISTRY.get(cli_name)
    return info.display_name if info else cli_name.capitalize()


def list_cli_names() -> list[str]:
    """List all registered CLI names."""
    return list(CLI_REGISTRY.keys())
