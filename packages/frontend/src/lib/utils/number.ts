/**
 * Returns a number whose value is limited to the given range.
 *
 * @param {Number} value The initial value to clamp.
 * @param {Number} min The lower boundary of the range.
 * @param {Number} max The upper boundary of the range.
 * @returns {Number} A number within the specified range (min, max).
 */
export function clamp(value: number, min: number, max: number): number {
	return Math.min(Math.max(value, min), max);
}
