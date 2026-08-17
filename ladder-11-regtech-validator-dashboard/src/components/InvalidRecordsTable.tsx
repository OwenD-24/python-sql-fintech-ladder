import type { ValidationRecord } from "../types/validation";

type InvalidRecordsTableProps = {
    records: ValidationRecord[]
}

function InvalidRecordsTable({ records }: InvalidRecordsTableProps) {
    return (
        <section className="records-section">
            <h2>Invalid Records</h2>

            <table>
                <thead>
                    <tr>
                        <th>Row</th>
                        <th>Transaction ID</th>
                        <th>Amount</th>
                        <th>Currency</th>
                        <th>Errors</th>
                    </tr>
                </thead>

                <tbody>
                    {records.map(record => (
                        <tr key={record.rowNumber}>
                            <td>{record.rowNumber}</td>
                            <td>{record.id || "Missing ID"}</td>
                            <td>{record.amount}</td>
                            <td>{record.currency}</td>
                            <td>{record.errors.join(", ")}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </section>
    )
}

export default InvalidRecordsTable