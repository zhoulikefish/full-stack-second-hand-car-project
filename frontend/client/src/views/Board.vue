<template>
    <!--渲染Echarts图表的容器-->
    <div>
		<Line></Line>
	</div>
</template>

<script>
import PriceTime from "../components/PriceTime.vue"
import Sun from "../components/Sun.vue"
import Line from "../components/Line.vue"

export default {
  name: "sun",
  components: {
    PriceTime,
	Sun,
	Line
}
};
</script>

<style>
    #main{
        width: 800px;
        height: 500px;
    }
</style>