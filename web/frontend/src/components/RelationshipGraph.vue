<template>
  <div class="charts" id="chart"></div>
</template>

<style lang="scss">
.charts {
  max-width: 100%;
  width: 100%;
  height: 500px;
  > canvas {
    max-width: 100%;
    width: 100%;
  }
  > div:first-child {
    max-width: 100%;
    width: 100% !important;
  }
}
canvas {
  max-width: 100%;
  width: 100% !important;
}
</style>

<script>
let echarts = require("echarts");
// import config from 'echarts/config';

import dataTool from "echarts/dist/extension/dataTool";
import axios from "axios";

export default {
  props: ["url", "graphMethod"],
  data() {
    return {
      dataUrl: this.url,
      screenWidth: document.body.clientWidth
    };
  },
  created() {},
  mounted() {
    window.onresize = () => {
      updateGraph();
    };
  },
  watch: {
    value(v) {
      this.dataUrl = v;
    },
    screenWidth(val) {
      this.screenWidth = val;
    }
  },
  mounted() {
    this.updateGraph();
  },
  methods: {
    updateGraph() {
      let myChart = echarts.init(document.getElementById("chart"));
      myChart.hideLoading();
      axios
        .get(this.dataUrl)
        .then(xml => {
          let categories = [];
          let option = {};
          let i = 0;
          xml.data.data.categories.map(name => {
            categories[i] = {
              name: name
            };
            i++;
          });
          console.log(xml.data);
          let graph = echarts.dataTool.gexf.parse(xml.data.data.graphData);
          console.log(graph);
          if (this.graphMethod == 1) {
            graph.nodes.map(node => {
              (node.itemStyle = null), (node.value = node.symbolSize);
              node.symbolSize /= 1.5;
              (node.label = {
                normal: {
                  show: node.symbolSize > 30
                }
              }),
                // (node.category = node.attributes.modularity_class);
                (node.draggable = true);
            });
            option = {
              title: {
                text: "知识点",
                subtext: "知识点",
                top: "bottom",
                left: "right"
              },
              tooltip: {},
              legend: [
                {
                  // data: categories.map(a => {
                  //   return a.name;
                  // })
                }
              ],
              animationDuration: 1500,
              animationEasingUpdate: "quintcInOut",
              series: [
                {
                  name: "KG_Education",
                  type: "graph",
                  layout: "none",
                  data: graph.nodes,
                  links: graph.links,
                  // categories: categories,
                  roam: true,
                  focuNodeAdjacency: true,
                  itemStyle: {
                    normal: {
                      borderColor: "#fff",
                      borderWidth: 1,
                      shadowBlur: 10,
                      shadowColor: "rgba(0,0,0,0.3)"
                    }
                  },
                  label: {
                    position: "right",
                    formatter: "{b}"
                  },
                  lineStyle: {
                    color: "source",
                     type: 'dashed',
                    curveness: 0.3
                  },
                  edgeSymbol: 'arrow', 
                  emhasis: {
                    lineStyle: {
                      width: 10
                    }
                  }
                }
              ]
            };
          } else {
            graph.nodes.map(node => {
              (node.itemStyle = null), (node.value = node.symbolSize);
              node.symbolSize = 60;
              (node.label = {
                normal: {
                  show: 1 //node.symbolSize > 30
                }
              }),
                (node.category = node.attributes.modularity_class);
              node.draggable = true;
            });
            option = {
              title: {
                text: "知识点",
                subtext: "知识点",
                top: "bottom",
                left: "right"
              },
              tooltip: {},
              legend: [
                {
                  data: categories.map(a => {
                    return a.name;
                  })
                }
              ],
              animation: false,
              focuNodeAdjacency: true,
              series: {
                name: "知识点",
                type: "graph",
                layout: "force",
                data: graph.nodes,
                links: graph.links,
                categories: categories,
                roam: true,
                label: {
                  prosition: "right",
                },
                edgeSymbol: 'arrow', 
                force: {
                  edgeLength: 100,
                  repulsion: 100
                }
              }
            };
          }
          myChart.setOption(option);
          // var ecConfig = require('echarts/config');
          myChart.on("click", params => {
            if (params.dataType == "node") {
              let name = params.data.name;
              console.log(name);
              this.$router.push(`/wiki/${name}`);
            }
          });
        })
        .catch(err => {
          console.log(err);
          this.$Message.error("数据加载失败");
        });
    }
  }
};
</script>