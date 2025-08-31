

// eslint-disable-next-line @typescript-eslint/no-explicit-any
function fallback(value: any, fallback: any) {
    return value === undefined ? fallback : value
}

type tFlyFadeOptions = {
    duration?: number,
    start?: number,
    end?: number,
    intro?: boolean,
}

/**
 * 
 * @param node Element to be animated
 * @param options
 * @returns 
 */
export function flyfade(
	node: Element,
	options: tFlyFadeOptions = {
		duration: 1000,
		start: 0,
		end: 0,
		intro: false
	}
) {

    // Get Fallback Values
    const duration = fallback(options.duration, 1000);
    const start = fallback(options.start, 0);
    const end = fallback(options.end, 0);
    const intro = fallback(options.intro, false);

	return {
		duration,
		css: (t: number) => {
			const tt = intro ? t : 1 - t;
			const y = start + (end - start) * tt;
			return `
                  opacity: ${t};
                  transform: translate3d(0, ${y}px, 0);
                `;
		}
	};
}
