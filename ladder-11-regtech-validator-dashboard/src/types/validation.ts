// The Python validator classifiies transaction records. 
// These TypeScript types describe the shape of those validation results for the React dashboard.
export type ValidationStatus =
 | "valid"
 | "review"
 | "invalid"

export type ValidationErrorType = 
 | "missing-id"
 | "invalid-amount"
 | "unsupported-currency"
 | "duplicate-id"

export type ValidationRecord = {
    rowNumber: number
    id: string
    amount: number
    currency: string
    status: ValidationStatus
    errors: ValidationErrorType[]
}