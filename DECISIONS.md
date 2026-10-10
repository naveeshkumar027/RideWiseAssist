# RideWise Assist — Design Decisions

## Architecture

The prototype uses Streamlit for the chat interface, Python for application logic, SQLite for the supplied records, PDF extraction and OCR for policy retrieval, and the authorised NeoStats-compatible LLM API for responses.

This design keeps the application locally runnable and small enough to develop and demonstrate quickly.

## Database access

The supplied database is opened in read-only mode, with SQLite query-only enabled. Parameterised queries retrieve records associated with the selected customer. The application does not intentionally modify the supplied database.

Customer selection is a demonstration mechanism, not identity verification.

## Policy retrieval

PDF pages are processed individually. Digital text is extracted directly, and OCR attempts to recover text embedded in scanned images.

A lightweight keyword-based scoring approach ranks policy passages. Relevant exceptions, such as the Gold-tier grace period, receive additional priority when the question concerns late returns and customer tiers.

A separate vector database was deferred to reduce setup complexity. Keyword ranking can miss relevant passages, so retrieval and policy reasoning require scenario testing.

## LLM grounding

The application sends the selected customer's context, relevant policy extracts, and conversation history to the configured NeoStats-compatible API. Its instructions emphasise evidence, policy exceptions, effective dates, privacy, and uncertainty.

Prompt instructions alone cannot guarantee correct answers. Responses must be validated against the database and source policies.

## Rejected alternatives

- Writable database access was rejected to preserve the supplied records.
- Other LLM providers and models were rejected to respect the hackathon constraints.
- Complex retrieval infrastructure was deferred for the initial prototype.
- Treating customer selection as authentication was rejected because identity is not verified.

## Failure modes

- Missing files: report the problem instead of inventing evidence.
- OCR failures: log the affected document and page.
- API errors: show a safe error message without exposing credentials.
- Policy-version conflicts: disclose uncertainty if the applicable version cannot be established.
- Missed exceptions: prioritise exception passages and test edge cases.
- Privacy risk: restrict database context to the selected customer.

## Next-week plan

1. Build repeatable tests for bookings, payments, refunds, cancellations, late returns, tier benefits, EV battery fees, and damage claims.
2. Verify policy-version selection and effective-date boundaries.
3. Improve retrieval and source traceability.
4. Add deterministic calculation checks where the data and rules permit them.
5. Test missing records, API failures, OCR failures, and ambiguous questions.
6. Verify a clean setup and inspect the Git repository for secrets before submission.