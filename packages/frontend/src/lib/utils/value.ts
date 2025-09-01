/* eslint-disable @typescript-eslint/no-explicit-any */

/**
 * Returns `value` or `fallback` if `value` is undefined
 * 
 * @param value - Checked Value
 * @param fallback - Fallback Value
 * @returns `fallback` if `value` is undefined, else `value`
 */
export function fallback(value: any, fallback: any) {
    return value === undefined ? fallback : value
}