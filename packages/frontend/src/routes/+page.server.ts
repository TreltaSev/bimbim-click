import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch, cookies, getClientAddress }) => {
	const ip = getClientAddress();

	const response = await fetch('http://backend:4000/click', {
		headers: {
			'X-Forwarded-For-Diff': ip
		}
	});

	let ipCount = 0;
	let totalCount = 0;

	if (response.status == 200) {
		const json = await response.json();
		ipCount = json.ip || 0;
		totalCount = json.total || 0;
	}

	return {
		clicks: {
			local: Number(cookies.get('clicks')) || 0,
			ip: ipCount,
			total: totalCount
		}
	};
};
