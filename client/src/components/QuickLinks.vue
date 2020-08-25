<template>
    <div>
        <b-card bg-variant="dark"
                header="Quick Links"
                text-variant="white"
                class="text-center links-card">
            <b-card-text>
                <a target="_blank" rel="noopener noreferrer" href="https://voteupapp.com/" class="quicklink">VoteUp</a>
            </b-card-text>
            <b-card-text>
                <a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/" class="quicklink">YouTube</a>
            </b-card-text>
            <b-card-text>
                <a target="_blank" rel="noopener noreferrer" href="https://www.imdb.com/" class="quicklink">IMDb</a>
            </b-card-text>
        </b-card>
    </div>
</template>

<style>
a.quicklink {
  color: white;
  text-decoration: none;
}

a.quicklink:hover {
    color: black;
}

div.linkscontaienr {
  width: 900px;
  margin: auto;
}

.links-card {
    max-width: 300px;
}
</style>
