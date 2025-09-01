import { fallback } from '@utils';
import type { TransitionConfig } from 'svelte/transition';

type tRotationOptions = {
	duration?: number;
	start?: number;
	end?: number;
};

/**
 * Makes the selected element rotate with given `options`
 *
 * @param node Element to be animation
 * @param options Animation options
 * @returns rotation transition
 */
export function rotation(node?: HTMLElement, options?: tRotationOptions): TransitionConfig {
	if (node === undefined) return {};
    
    const duration = fallback(options?.duration, 1000);
	const start = fallback(options?.start, 0);
	const end = fallback(options?.end, 360);

	let phase: 'in' | 'out' | null = null;

	function getRotation(t: number, u: number): number {
		// Save Phase
		if (phase == null) {
			phase = t < 0.5 ? 'in' : 'out';
		}

		const tt = phase == 'in' ? t : u;

		switch (phase) {
			case 'in':
				return start + (end / 2 - start) * tt;
			case 'out':
				return end / 2 + (end - end / 2) * tt;
			default:
				return 0;
		}
	}

	return {
		duration,

        css: (t: number, u: number) => {
            const rotation = getRotation(t, u);
            return `transform: rotate(${rotation}deg)`
        },

        tick: (t: number, u: number) => {
            const rotation = getRotation(t, u);
            node.style.transform = `rotate(${rotation}deg)`
        }
	};
}
