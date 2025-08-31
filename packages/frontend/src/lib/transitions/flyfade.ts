export function flyfade(
	node: Element,
	{
		duration,
		start = 0,
		end = 0,
		intro = false
	}: { duration: number; start?: number; end?: number; intro?: boolean }
) {
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
