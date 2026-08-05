// This mock array represents validation results that would normally come from the Python backend.
// TypeScript checks that every record follows the expected dashboard data shape.
import type { ValidationRecord } from "../types/validation"

export const mockValidationResults: ValidationRecord[] = [
    {
        rowNumber: 2,
        id: "TXN001",
        amount: 250,
        currency: "GBP",
        status: "valid",
        errors: []
    },
    {
        rowNumber: 3,
        id: "TXN002",
        amount: -50,
        currency: "GBP",
        status: "invalid",
        errors: ["invalid-amount"] 
    },
    {
        rowNumber: 4,
        id: "TXN003",
        amount: 8000,
        currency: "USD",
        status: "review",
        errors: []
    },
    {
        rowNumber: 5,
        id: "TXN002",
        amount: 1800,
        currency: "EUR",
        status: "invalid",
        errors: ["duplicate-id"]
    },
    {
        rowNumber: 6,
        id: "",
        amount: 800,
        currency: "CAD",
        status: "invalid",
        errors: ["missing-id", "unsupported-currency"]
    }
]