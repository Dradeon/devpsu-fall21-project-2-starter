<template>
    <div>
        <main>
            <h2 class = "cover-heading">Your Personal Journal:</h2>
            <JournalArea/>
        </main>
    </div>
    
</template>

<script>
import JournalArea from '@/components/JournalArea.vue'

export default {
  components: { JournalArea },
    name: 'journal'
}
</script>
