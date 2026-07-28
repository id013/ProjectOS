# Матрица покрытия мастер-документа

| Раздел требования | Реализация | Статус |
|---|---|---|
| 1. Главная цель | `README.md`, архитектура, lifecycle | Covered |
| 2. Принципы | README: неподвижные правила; architecture/context/QA | Covered |
| 3. Контекст пользователя | уровни сложности; Crynet; batch; security | Covered |
| 4.1 Архитектура | `docs/01_architecture.md` | Covered |
| 4.2 Жизненный цикл | `docs/02_lifecycle.md` | Covered |
| 4.3 A–O шаблоны | `templates/core_artifacts.md` | Covered |
| 5. Работа с чатами | `docs/03_work_protocol.md`, session templates | Covered / адаптировано к Work task |
| 6. Context Engineering | `docs/04_context_engineering.md`, Context Manifest | Covered |
| 7. Противоречия/устаревание | `docs/05_audit_and_versioning.md` | Covered |
| 8. Quality Gate + 12 областей | `docs/06_quality_gates.md`, `checklists/domain_quality.md` | Covered |
| 9. Массовый конвейер | `docs/07_batch_pipeline.md` | Covered |
| 10. Роли/автоматизации | `docs/08_roles_and_automation.md` | Covered |
| 11. Bootstrap | `docs/09_bootstrap.md` | Covered |
| 12. Ежедневные команды | `docs/10_daily_commands.md` | Covered |
| 13. Steward Mode | `templates/session_templa…47971 tokens truncated…"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Path to report JSON")
    parser.add_argument("output", type=Path, help="Path to output HTML")
    args = parser.parse_args()

    with args.input.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise SystemExit("Input JSON must contain an object at the top level.")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(build_html(data), encoding="utf-8")
    print(f"Created report: {args.output.resolve()}")


if __name__ == "__main__":
    main()
