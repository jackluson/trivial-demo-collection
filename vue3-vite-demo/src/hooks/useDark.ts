/*
 * @Date: 2021-10-18 20:35:32
 * @LastEditTime: 2021-10-20 11:33:10
 * @Description: 
 */

import { ref, watch, computed, onUnmounted } from 'vue'

export function useDark() {
  const system = usePreferDark()
  console.log("🚀 ~ useDark ~ system", system)
  const setting = useLocalStorage('setting-dark', 'auto')

  const dark = computed({
    get() {
      return setting.value === 'auto'
        ? system.value
        : setting.value === 'dark'
    },
    set(v) {
      if (v === system.value)
        setting.value = 'auto'
      else
        setting.value = v ? 'dark' : 'light'
    },
  })

  return dark
}

export function usePreferDark() {
  const media = window.matchMedia('(prefers-color-scheme: dark)')
  const dark = ref(media.matches)

  const update = () => dark.value = media.matches

  media.addEventListener('change', update)
  onUnmounted(() => {
    media.removeEventListener('change', update)
  })

  return dark
}

export function useLocalStorage(key: string, defaultValue: any) {
  const data = ref(localStorage.getItem(key) ?? defaultValue)

  watch(data, () => localStorage.setItem(key, data.value))

  return data
}
