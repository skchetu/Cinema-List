<template>
  <div>
    <b-alert variant="success" dismissible fade :show="showMessage" @dismissed="showMessage=false">
      {{ message }}
    </b-alert>
    <br>
  </div>
</template>

<script>
export default {
  props: ['message', 'showMessage'],
};
</script>
