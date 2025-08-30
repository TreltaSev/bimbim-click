<script lang="ts">
	import { Flex, Frame } from "sk-clib";

    async function postClick() {
        await fetch(`https://api.${window.location.host}/click`, {method: "POST", credentials: "same-origin"})
    }

</script>

<Flex center class="-mt-40" fill>
    <Frame onclick={() => postClick()} class="rounded-full cursor-pointer hover:bg-amber-200 hover:size-32  active:size-28 origin-center transform duration-200 ease-in-out bg-primary size-30">

    </Frame>
</Flex>