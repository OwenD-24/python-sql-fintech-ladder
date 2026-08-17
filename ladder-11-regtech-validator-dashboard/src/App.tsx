// The dashboard imports the typed validation results and filters them by status.
// Each summary card receives a label and the calculated count through props.
import "./App.css"
import { useState } from "react"
import SummaryCard from "./components/SummaryCard"
import { mockValidationResults } from "./data/mockValidationResults"
import InvalidRecordsTable from "./components/InvalidRecordsTable"
import type { ValidationErrorType } from "./types/validation"

type ErrorFilter = "all" | ValidationErrorType

function App() {
  const [selectedError, setSelectedError] = useState<ErrorFilter>("all")
  const totalCount = mockValidationResults.length

  const validCount = mockValidationResults.filter(
    record => record.status === "valid"
  ).length

  const reviewCount = mockValidationResults.filter(
    record => record.status === "review"
  ).length

  const invalidCount = mockValidationResults.filter(
    record => record.status === "invalid"
  ).length

  const invalidRecords = mockValidationResults.filter(
    record => record.status === "invalid"
  )

  const filteredInvalidRecords = 
  selectedError === "all"
  ? invalidRecords
  : invalidRecords.filter(record =>
    record.errors.includes(selectedError)
  )

  return (
    <main className="dashboard">
      <header>
        <p className="eyebrow">RegTech Submission Validator</p>
        <h1>Validation Dashboard</h1>
        <p>
          Review transaction validation results produced by the Python validator.
        </p>
      </header>

      <section className="summary-grid">
        <SummaryCard label="Total records" count={totalCount} />
        <SummaryCard label="Valid" count={validCount} />
        <SummaryCard label="Review" count={reviewCount} />
        <SummaryCard label="Invalid" count={invalidCount} />
      </section>

      <section className="filter-section">
        <label htmlFor="error-filter">Filter by error type:</label>

        <select
          id="error-filter"
          value={selectedError}
          onChange={event =>
            setSelectedError(event.target.value as ErrorFilter)
          }>
            <option value="all">All errors</option>
            <option value="missing-id">Missing ID</option>
            <option value="invalid-amount">Invalid amount</option>
            <option value="unsupported-currency">Unsupported currency</option>
            <option value="duplicate-id">Duplicate ID</option>
          </select>
      </section>

      <section className="upload-section">
        <h2>Upload Submission</h2>

        <input type="file" accept=".csv" />

        <button type="button">
          Validate File
        </button>
      </section>

      <InvalidRecordsTable records={filteredInvalidRecords} />
    </main>
  )
  
}

export default App