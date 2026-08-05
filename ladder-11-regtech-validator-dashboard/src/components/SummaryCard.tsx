// SummaryCardProps defines the values the component must receive.
// Each summary card receives a text label and a numeric count.
type SummaryCardProps = {
    label: string
    count: number
}

function SummaryCard({ label, count }: SummaryCardProps) {
    return (
        <article className="summary-card">
            <p>{label}</p>
            <strong>{count}</strong>
        </article>
    )
}

export default SummaryCard