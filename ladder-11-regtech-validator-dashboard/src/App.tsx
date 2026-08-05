// The dashboard imports the typed validation results and filters them by status.
// Each summary card receives a label and the calculated count through props.
import "./App.css"
import SummaryCard from "./components/SummaryCard"
import { mockValidationResults } from "./data/mockValidationResults"

function App() {
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
    </main>
  )
  
}

export default App