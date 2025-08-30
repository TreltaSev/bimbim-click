<script lang="ts">
	import { Flex, Frame, Spacer, Text } from 'sk-clib';
	import type { PageProps } from './$types';
	import { onMount } from 'svelte';

	let { data }: PageProps = $props();

	let socket: WebSocket | undefined = $state(undefined);

	let localClicks: number = $state(data.clicks.local);
	let totalClicks: number = $state(data.clicks.total);

	// Update cookies with local clicks
	$effect(() => {
		const expires = new Date();
		expires.setFullYear(expires.getFullYear() + 10);
		document.cookie = `clicks=${localClicks}; expires=${expires.toUTCString()}; path=/`;
	});

	function iterCounter() {
		// Update local click counter
		localClicks++;

		// Add to total clicks
		totalClicks++;
	}

	function deiterCounter() {
		localClicks--;
		totalClicks--;
	}

	function deltaCounter(amount: number) {
		totalClicks += amount;
	}

	async function postClick() {
		iterCounter();
		if (socket) {
			socket.send(JSON.stringify({ operation: 'click' }));
		}
	}

	onMount(() => {
		socket = new WebSocket(`wss://api.${window.location.host}/click`);

		socket.onmessage = (ev) => {
			const _json = JSON.parse(ev.data);
			const operation = _json.operation;
			switch (operation) {
				case 'click':
					const ok = _json.ok;
					if (!ok) {
						deiterCounter();
					}
					break;
				case 'update':
					const delta = _json.delta;
					deltaCounter(delta);
					break;
			}
		};
	});
</script>

<Flex fillw row class="box-border gap-5 p-5">
	<Spacer width />

	<Flex row class="gap-2 rounded-xl p-3" tertiary>
		<Text class="whitespace-nowrap">Your Clicks:</Text>
		<Text class="whitespace-nowrap">{localClicks}</Text>
	</Flex>

	<Flex row class="gap-2 rounded-xl p-3" tertiary>
		<Text class="whitespace-nowrap">Total Clicks:</Text>
		<Text class="whitespace-nowrap">{totalClicks}</Text>
	</Flex>
</Flex>

<Flex center class="-mt-40" fill>
	<Frame
		onclick={() => postClick()}
		class={`
        bg-primary ease-in-outs size-30 cursor-pointer
        rounded-full shadow-2xl
        duration-200
        hover:size-32
        hover:bg-amber-200 active:size-28
    `}
	/>
</Flex>
