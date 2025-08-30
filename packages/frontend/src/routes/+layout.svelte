<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';

	import {ThemeInit} from "sk-clib/theme";
	import { Flex } from 'sk-clib';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<ThemeInit defaults={{
	defaultMode: "dark",
	defaultVariant: "neutral",
	defaultSeedColor: "#f79763"
}}/>

<Flex fill col background>
	{@render children?.()}
</Flex>
