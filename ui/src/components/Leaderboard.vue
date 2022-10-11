<script setup>
    import { ref, onBeforeMount} from "vue";
    import { useRouter, useRoute } from "vue-router";
    import Player from '../services/Player'

    const players = ref([])
    const router = useRouter()

    const getData = async () => {
        const response = await Player.getPlayers()
        players.value = response
        console.log(players.value)
    }

    onBeforeMount(() => {
        getData()
    })

    // use with vue query
    
    const route = useRoute();
    const client_id = Date.now();
    const text = ref("");
    const messages = ref([]);

    </script>
    
    <template>
      <div class="bg-quiz w-screen h-screen bg-no-repeat bg-cover text-white">
        <div class="p-10 ml-6 mr-6">
    
          <!--Header-->
          <div class="grid grid-rows-2 grid-flow-col gap-2">
            <router-link to="/">
              <div class="text-5xl font-semibold col-span-2">GameVerse</div>
            </router-link>
            <div class="text-2xl col-span-2">Leaderboard</div>
          </div>
          <div class="align-middle">
            <div class="text-2xl text-center font-bold mt-8">Overall Leaderboard</div>
            <div class="flex justify-center items-center mt-8 grid grid-flow-col auto-cols-max">
              <div>
                <div class="overflow-x-auto relative">
                    <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                            <tr>
                                <th scope="col" class="py-3 px-6">
                                    Position
                                </th>
                                <th scope="col" class="py-3 px-6">
                                    Employee name
                                </th>
                                <th scope="col" class="py-3 px-6">
                                    Score
                                </th>
                            </tr>
                        </thead>
                            <tbody v-for="(player, index) in players" :key="index">
                                <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                                    <th scope="row" class="py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                        {{player.id}}
                                    </th>
                                    <td class="py-4 px-6">
                                        {{player.name}}
                                    </td>
                                    <td class="py-4 px-6">
                                        {{player.total_points}}
                                    </td>
                                </tr>
                            </tbody>
                    </table>
                </div>
              </div>
            </div>
          </div>
          
        </div>
      </div>
    </template>