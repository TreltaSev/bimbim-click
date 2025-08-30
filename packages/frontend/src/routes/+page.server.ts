import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch, cookies }) => {

	const response = await fetch('http://backend:4000/click');

	let totalCount = 0;

	if (response.status == 200) {
		const json = await response.json();
		totalCount = json.total || 0;
	}

	return {
		clicks: {
			local: Number(cookies.get('clicks')) || 0,
			total: totalCount
		}
	};
};
