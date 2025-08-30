<script lang="ts">
	import { Flex, Frame, Spacer, Text } from "sk-clib";
    import type { PageProps } from "./$types";
	import { onMount } from "svelte";

    let { data }: PageProps = $props();

    let localClicks: number = $state(data.clicks.local);
    let ipClicks: number = $state(data.clicks.ip);
    let totalClicks: number = $state(data.clicks.total);

    // Update cookies with local clicks
    $effect(() => {
        const expires = new Date();
        expires.setFullYear(expires.getFullYear() + 10);
        document.cookie = `clicks=${localClicks}; expires=${expires.toUTCString()}; path=/`;
    })



    function iterCounter() {
        // Update local click counter
        localClicks++;

        // Add to ip clicks
        ipClicks++;

        // Add to total clicks
        totalClicks++;
    }

    async function postClick() {
        await fetch(`https://api.${window.location.host}/click`, {method: "POST", credentials: "same-origin"})
        iterCounter();
    }

    onMount(() => {
        console.log(data)
    })

</script>

<Flex fillw row class="box-border p-5 gap-5">
    <Spacer width/>

    <Flex row class="p-3 rounded-xl gap-2" tertiary>
        <Text class="whitespace-nowrap">Your Clicks:</Text>
        <Text class="whitespace-nowrap">{localClicks}</Text>
    </Flex>

    <Flex row class="p-3 rounded-xl gap-2" tertiary>
        <Text class="whitespace-nowrap">IP Clicks:</Text>
        <Text class="whitespace-nowrap">{ipClicks}</Text>
    </Flex>
    
    <Flex row class="p-3 rounded-xl gap-2" tertiary>
        <Text class="whitespace-nowrap">Total Clicks:</Text>
        <Text class="whitespace-nowrap">{totalClicks}</Text>
    </Flex>
</Flex>

<Flex center class="-mt-40" fill>
    <Frame onclick={() => postClick()} class={`
        bg-primary rounded-full size-30 shadow-2xl
        hover:bg-amber-200 hover:size-32
        active:size-28
        cursor-pointer
        duration-200 ease-in-outs
    `}/>
</Flex>