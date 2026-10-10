# RideWise Assist

RideWise Assist is a local conversational rental-support assistant built for the NeoStats AI Engineer Intern Hackathon.

## Features

- Streamlit chat interface with Customer and Support Agent roles.
- Customer-specific booking, payment, and damage-report retrieval.
- Read-only SQLite database access.
- PDF policy text extraction and OCR for scanned policy pages.
- Policy retrieval and NeoStats LLM-powered responses.
- Conversation history and new-conversation controls.

## Requirements

- Python 3.11 or newer.
- The supplied RideWise database, data dictionary, and policy PDFs.
- An authorised NeoStats API key and endpoint.
- Tesseract OCR installed for scanned policy pages.

## Windows setup

Run PowerShell from the project directory.

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   python -m pip install streamlit python-dotenv requests pypdf openai pytesseract pdf2image Pillow
   ```

3. Copy the example configuration:

   ```powershell
   Copy-Item .env.example .env
   ```

4. Open `.env` locally and set the authorised `NEOSTATS_API_KEY`. Keep this file private and never commit it.

5. Start the application:

   ```powershell
   streamlit run app.py
   ```

6. Open the local URL printed by Streamlit.

## Configuration

- `NEOSTATS_ENDPOINT`: authorised NeoStats-compatible API endpoint.
- `NEOSTATS_API_KEY`: authorised credential.
- `NEOSTATS_MODEL`: model identifier supplied for the hackathon.

The current OCR configuration expects Tesseract at `C:\Program Files\Tesseract-OCR\tesseract.exe`.

## Data and safety

The application opens SQLite in read-only mode and retrieves records for the selected customer. The customer selector is for demonstration only and does not authenticate identity. Policy retrieval and LLM responses can be incorrect; validate policy exceptions, effective dates, and calculations against the source documents.

## Validation

Check Python syntax:

```powershell
python -m py_compile app.py
```

If `test_policy.py` is present, run:

```powershell
python test_policy.py
```

Test bookings, refunds, cancellations, late-return grace periods, EV battery fees, damage claims, missing records, and policy-version boundaries before submission.

## Limitations

- Customer selection is not production authentication.
- Support Agent mode is limited to the selected customer's records.
- Keyword-based policy retrieval may miss relevant passages.
- API availability is required to generate answers.
- Broader scenario testing is still required.