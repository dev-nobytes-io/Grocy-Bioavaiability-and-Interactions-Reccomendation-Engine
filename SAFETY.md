# Safety

This project suggests changes to what people eat. Some of those suggestions can harm specific people. This page states what the software is for, what it will not do, how it protects people, and how to report a problem.

It replaces the original README's statement that there is no liability. That statement was not accurate in law, and it gave the project no way to protect anyone. See [claim C28](docs/research/claim-verification.md) and the [safety model](docs/science/safety-model.md).

## Intended purpose

> A personal, self-hosted tool that suggests what to add to, re-time, swap or skip in your meals to support recovery from training and general wellness. It works from the food you have at home and the health information you choose to give it, which it uses to keep suggestions safe, tolerable and suited to you. It does not diagnose, treat, cure or prevent any disease. It does not interpret medical test results.

Every feature, document and generated sentence must fit inside that statement. A change that needs a broader purpose needs a decision record first. See [GOVERNANCE.md](GOVERNANCE.md).

## Not medical advice

Nothing this project produces is medical advice. Talk to a clinician before acting on any suggestion if any of these apply to you:

- you take prescription medicine, especially blood thinners, anti-epileptic drugs, insulin or other glucose-lowering drugs;
- you have kidney disease, liver disease, iron overload (haemochromatosis) or G6PD deficiency;
- you are pregnant or breastfeeding;
- you have diabetes, gastroparesis, irritable bowel syndrome or an eating disorder;
- you have food allergies.

## How the software protects people

These are design commitments. They are specified in the [safety model](docs/science/safety-model.md).

1. **Gates run before ranking.** Every rule lists the groups it must never reach. The engine removes gated suggestions before it scores anything.
2. **Unknown means no.** If the engine does not know whether a gate applies, for example because you skipped the medication question, the gated suggestion does not appear.
3. **Evidence is shown.** Every suggestion shows its dose, its evidence grade and a link to its source.
4. **Supplement-dose findings are labelled.** Effects only shown at supplement doses are never presented as something a meal can achieve.
5. **Upper limits are tracked.** Suggested amounts are added to the supplements you declare and checked against tolerable upper intake levels.
6. **Health information shapes, never treats.** Conditions, intolerances, medicines and recent illness are used to withhold, adjust, swap or re-time suggestions. The engine never suggests a food as a treatment for a condition. See [ADR-0009](docs/decisions/0009-recovery-goal-and-health-profile.md).
7. **Your data stays home.** Health information never leaves the machine you run it on. There is no telemetry.

## What it will not do

- Diagnose a condition or tell you that a test result is normal or abnormal.
- Tell you to start, stop or change a medicine.
- Claim that a suggestion treats or prevents a disease.
- Send your health or inventory data anywhere.

Features that would cross these lines are out of scope. Examples include interpreting lab values or checking your medicines against each other. Adding one requires a decision record and a regulatory review. See [open questions](docs/open-questions.md).

## No warranty

The software is provided "as is", without warranty of any kind, under sections 7 and 8 of the [Apache License 2.0](LICENSE). The knowledge base carries the equivalent disclaimer in section 5 of [CC BY 4.0](knowledge/LICENSE). A licence disclaimer does not remove every legal duty. It does not replace the protections above.

## Reporting a safety problem

A safety problem is any suggestion that could harm someone. Examples: a rule that fires for a group it should be gated from, a wrong dose, a misread source, or a missing contraindication.

- **If it does not involve anyone's personal health details,** open a [safety concern issue](https://github.com/dev-nobytes-io/Grocy-Bioavaiability-and-Interactions-Reccomendation-Engine/issues/new?template=safety_concern.yml).
- **If it does,** report it privately through [GitHub private vulnerability reporting](https://github.com/dev-nobytes-io/Grocy-Bioavaiability-and-Interactions-Reccomendation-Engine/security/advisories/new). Do not post personal health information in public issues.

Safety reports take priority over all other work. A rule under a credible safety report is set to `in_review` and stops producing suggestions until the report is resolved.
