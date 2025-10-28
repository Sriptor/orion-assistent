#!/usr/bin/env python3
"""Orion Voice Assistant - Main Entry Point"""

from src.orion.assistant import OrionAssistant


def main():
    """Main function"""
    assistant = OrionAssistant()
    assistant.run()


if __name__ == "__main__":
    main()