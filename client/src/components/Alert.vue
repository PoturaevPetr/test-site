<template>
	<div>
		<b-alert variant="succsess" show>{{ message }}</b-alert>
	</div>
</template>

<script>
export default {
  props: ['message'],
};
</script>