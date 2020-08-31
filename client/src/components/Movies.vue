<template>
  <div class="container">
    <div class="row">
      <div class="col-lg-10 m-a">
        <div class="container">
          <div class="row">
            <div class="col-sm-10 m-a">
              <h1>Film Ratings</h1>
              <hr />
              <br />
              <br />
              <alert :message="message" :showMessage="showMessage"></alert>
              <button type="button" class="btn btn-dark btn-sm" v-b-modal.movie-modal>
                <font-awesome-icon icon="plus"></font-awesome-icon>
              </button>
              <br />
              <br />
              <table class="table table-hover">
                <thead>
                  <tr>
                    <th scope="col">Week of...</th>
                    <th scope="col">Title</th>
                    <th scope="col">Director(s)</th>
                    <th scope="col">S</th>
                    <th scope="col">C</th>
                    <th scope="col">A</th>
                    <th scope="col">Avg</th>
                    <th></th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(movie, index) in movies" :key="index">
                    <td>{{ movie.week }}</td>
                    <td>{{ movie.title }}</td>
                    <td>{{ movie.director }}</td>
                    <td>{{ movie.shanRating }}</td>
                    <td>{{ movie.cheRating }}</td>
                    <td>{{ movie.andhiRating }}</td>
                    <td>{{ movie.avgRating }}</td>
                    <td>
                      <div class="btn-group" role="group">
                        <button
                          type="button"
                          class="btn btn-outline-dark btn-sm"
                          v-b-modal.movie-update-modal
                          @click="editMovie(movie)"
                        ><font-awesome-icon icon="pen"></font-awesome-icon></button>
                        <button
                          type="button"
                          class="btn btn-dark btn-sm"
                          @click="onDeleteMovie(movie)"
                        ><font-awesome-icon icon="trash"></font-awesome-icon></button>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <v-card>
            <v-card-title>
              Ratings
              <v-btn color="primary"
                      dark
                      class="mb-2"
                      v-bind="attrs"
                      v-on="on"
                    ><font-awesome-icon icon="plus"></font-awesome-icon></v-btn>
            </v-card-title>
            <v-data-table
              :headers="headers"
              :items="movies"
              :search="search"
              hide-default-footer
            ></v-data-table>
          </v-card>
          <!-- <datatable :headers="headers" :items="movies" :search="search"></datatable> -->
          <br/>
          <v-card>
            <v-card-title>
              Ratings
              <v-btn color="primary"
                      dark
                      class="mb-2"
                      v-bind="attrs"
                      v-on="on"
                    ><font-awesome-icon icon="plus"></font-awesome-icon></v-btn>
            </v-card-title>
            <v-data-table
              :headers="headers"
              :items="movies"
              :search="search"
              hide-default-footer
            >
              <template v-slot:[`item.action`]="{{ item }}">
            </v-data-table>
          </v-card>
          <b-modal ref="addMovieModal" id="movie-modal" title="Add a new movie" hide-footer>
            <b-form @submit="onSubmit" @reset="onReset" class="w-100">
              <b-form-group id="form-week-group" label="Week of:" label-for="form-week-input">
                <b-form-input
                  id="form-week-input"
                  type="date"
                  v-model="addMovieForm.week"
                  required
                  placeholder="Enter week"
                ></b-form-input>
              </b-form-group>
              <b-form-group id="form-title-group" label="Title:" label-for="form-title-input">
                <b-form-input
                  id="form-title-input"
                  type="text"
                  v-model="addMovieForm.title"
                  required
                  placeholder="Enter title"
                ></b-form-input>
              </b-form-group>
              <b-form-group id="form-director-group"
                            label="Director(s):"
                            label-for="form-director-input">
                <b-form-input
                  id="form-director-input"
                  type="text"
                  v-model="addMovieForm.director"
                  placeholder="Enter director(s)"
                ></b-form-input>
              </b-form-group>
              <b-form-group
                id="form-shanRating-group"
                label="Shan's Rating:"
                label-for="form-shanRating-input"
              >
                <b-row>
                  <b-col sm="1">
                    <span class="range-value-color">{{ addMovieForm.shanRating }}</span>
                  </b-col>
                  <b-col sm="10">
                    <b-form-input
                      id="form-shanRating-input"
                      type="range"
                      min="0"
                      max="10"
                      step="0.25"
                      v-model="addMovieForm.shanRating"
                      required
                      placeholder="Enter rating"
                    ></b-form-input>
                  </b-col>
                </b-row>
              </b-form-group>
              <b-form-group
                id="form-cheRating-group"
                label="Che's Rating:"
                label-for="form-cheRating-input"
              >
                <b-row>
                  <b-col sm="1">
                    <span class="range-value-color">{{ addMovieForm.cheRating }}</span>
                  </b-col>
                  <b-col sm="10">
                    <b-form-input
                      id="form-cheRating-input"
                      type="range"
                      min="0"
                      max="10"
                      step="0.25"
                      v-model="addMovieForm.cheRating"
                      required
                      placeholder="Enter rating"
                    ></b-form-input>
                  </b-col>
                </b-row>
              </b-form-group>
              <b-form-group
                id="form-andhiRating-group"
                label="Andhi's Rating:"
                label-for="form-andhiRating-input"
              >
                <b-row>
                  <b-col sm="1">
                    <span class="range-value-color">{{ addMovieForm.andhiRating }}</span>
                  </b-col>
                  <b-col sm="10">
                    <b-form-input
                      id="form-andhiRating-input"
                      type="range"
                      min="0"
                      max="10"
                      step="0.25"
                      v-model="addMovieForm.andhiRating"
                      required
                      placeholder="Enter rating"
                    ></b-form-input>
                  </b-col>
                </b-row>
              </b-form-group>
              <b-button-group>
                <b-button type="submit" variant="outline-dark">Submit</b-button>
                <b-button type="reset" variant="dark">Reset</b-button>
              </b-button-group>
            </b-form>
          </b-modal>
          <b-modal ref="editMovieModal" id="movie-update-modal" title="Update" hide-footer>
            <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
              <b-form-group id="form-week-edit-group"
                            label="Week of:"
                            label-for="form-week-edit-input">
                <b-form-input
                  id="form-week-edit-input"
                  type="date"
                  v-model="editForm.week"
                  required
                  placeholder="Enter week"
                ></b-form-input>
              </b-form-group>
              <b-form-group id="form-title-edit-group"
                            label="Title:"
                            label-for="form-title-edit-input">
                <b-form-input
                  id="form-title-edit-input"
                  type="text"
                  v-model="editForm.title"
                  required
                  placeholder="Enter title"
                ></b-form-input>
              </b-form-group>
              <b-form-group
                id="form-director-edit-group"
                label="Director(s):"
                label-for="form-director-edit-input"
              >
                <b-form-input
                  id="form-director-edit-input"
                  type="text"
                  v-model="editForm.director"
                  required
                  placeholder="Enter director"
                ></b-form-input>
              </b-form-group>
              <b-form-group
                id="form-shanRating-edit-group"
                label="Shan's Rating:"
                label-for="form-shanRating-edit-input"
              >
                <b-row>
                  <b-col sm="1">
                    <span class="range-value-color">{{ editForm.shanRating }}</span>
                  </b-col>
                  <b-col sm="10">
                    <b-form-input
                      id="form-shanRating-edit-input"
                      type="range"
                      min="0"
                      max="10"
                      step="0.25"
                      v-model="editForm.shanRating"
                      required
                      placeholder="Enter rating"
                    ></b-form-input>
                  </b-col>
                </b-row>
              </b-form-group>
              <b-form-group
                id="form-cheRating-edit-group"
                label="Che's Rating:"
                label-for="form-cheRating-edit-input"
              >
                <b-row>
                  <b-col sm="1">
                    <span class="range-value-color">{{ editForm.cheRating }}</span>
                  </b-col>
                  <b-col sm="10">
                    <b-form-input
                      id="form-cheRating-edit-input"
                      type="range"
                      min="0"
                      max="10"
                      step="0.25"
                      v-model="editForm.cheRating"
                      required
                      placeholder="Enter rating"
                    ></b-form-input>
                  </b-col>
                </b-row>
              </b-form-group>
              <b-form-group
                id="form-andhiRating-edit-group"
                label="Andhi's Rating:"
                label-for="form-andhiRating-edit-input"
              >
                <b-row>
                  <b-col sm="1">
                    <span class="range-value-color">{{ editForm.andhiRating }}</span>
                  </b-col>
                  <b-col sm="10">
                    <b-form-input
                      id="form-andhiRating-edit-input"
                      type="range"
                      min="0"
                      max="10"
                      step="0.25"
                      v-model="editForm.andhiRating"
                      required
                      placeholder="Enter rating"
                    ></b-form-input>
                  </b-col>
                </b-row>
              </b-form-group>
              <b-button-group>
                <b-button type="submit" variant="outline-dark">Update</b-button>
                <b-button type="reset" variant="dark">Cancel</b-button>
              </b-button-group>
            </b-form>
          </b-modal>
        </div>
      </div>
      <div class="col-lg-2 m-a">
        <quicklinks></quicklinks>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import moment from 'moment';
import Alert from './Alert.vue';
import QuickLinks from './QuickLinks.vue';

export default {
  data() {
    return {
      search: '',
      headers: [
        {
          text: 'Title',
          align: 'start',
          value: 'title',
        },
        { text: 'Director(s)', value: 'director' },
        { text: 'Watch Week', value: 'week' },
        { text: 'Shantanu\'s', value: 'shanRating' },
        { text: 'Chetu\'s', value: 'cheRating' },
        { text: 'Andhi\'s', value: 'andhiRating' },
        { text: 'AVG', value: 'avgRating' },
        { text: 'Actions' },
      ],
      desserts: [
        {
          name: 'Frozen Yogurt',
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: '1%',
        },
        {
          name: 'Ice cream sandwich',
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: '1%',
        },
        {
          name: 'Eclair',
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          iron: '7%',
        },
        {
          name: 'Cupcake',
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          iron: '8%',
        },
        {
          name: 'Gingerbread',
          calories: 356,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          iron: '16%',
        },
        {
          name: 'Jelly bean',
          calories: 375,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
          iron: '0%',
        },
        {
          name: 'Lollipop',
          calories: 392,
          fat: 0.2,
          carbs: 98,
          protein: 0,
          iron: '2%',
        },
        {
          name: 'Honeycomb',
          calories: 408,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
          iron: '45%',
        },
        {
          name: 'Donut',
          calories: 452,
          fat: 25.0,
          carbs: 51,
          protein: 4.9,
          iron: '22%',
        },
        {
          name: 'KitKat',
          calories: 518,
          fat: 26.0,
          carbs: 65,
          protein: 7,
          iron: '6%',
        },
      ],
      movies: [],
      addMovieForm: {
        week: '',
        title: '',
        director: '',
        shanRating: '',
        cheRating: '',
        andhiRating: '',
        avgRaing: '',
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        week: '',
        title: '',
        director: '',
        shanRating: '',
        cheRating: '',
        andhiRating: '',
        avgRating: '',
      },
    };
  },
  components: {
    alert: Alert,
    quicklinks: QuickLinks,
  },
  methods: {
    getMovies() {
      const path = 'http://localhost:5000/movies';
      axios
        .get(path)
        .then((res) => {
          this.movies = res.data.movies;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addMovie(payload) {
      const path = 'http://localhost:5000/movies';
      axios
        .post(path, payload)
        .then(() => {
          this.getMovies();
          this.message = 'Movie added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getMovies();
        });
    },
    initForm() {
      this.addMovieForm.week = '';
      this.addMovieForm.title = '';
      this.addMovieForm.director = '';
      this.addMovieForm.shanRating = '';
      this.addMovieForm.cheRating = '';
      this.addMovieForm.andhiRating = '';
      this.editForm.id = '';
      this.editForm.week = '';
      this.editForm.title = '';
      this.editForm.director = '';
      this.editForm.shanRating = '';
      this.editForm.cheRating = '';
      this.editForm.andhiRating = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addMovieModal.hide();

      const weekFormatted = moment(this.addMovieForm.week).format('MMM Do');
      const sRating = this.addMovieForm.shanRating
        ? this.addMovieForm.shanRating
        : '0';
      const cRating = this.addMovieForm.cheRating
        ? this.addMovieForm.cheRating
        : '0';
      const aRating = this.addMovieForm.andhiRating
        ? this.addMovieForm.andhiRating
        : '0';
      const avg = ((parseFloat(sRating) + parseFloat(cRating)
        + parseFloat(aRating)) / 3).toFixed(2);

      const payload = {
        week: weekFormatted,
        title: this.addMovieForm.title,
        director: this.addMovieForm.director,
        shanRating: sRating,
        cheRating: cRating,
        andhiRating: aRating,
        avgRating: avg,
      };
      this.addMovie(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addMovieModal.hide();
      this.initForm();
    },
    editMovie(movie) {
      this.editForm = movie;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editMovieModal.hide();
      // test comment
      // let read = false;
      // if (this.editForm.read[0]) read = true;

      const weekFormatted = moment(this.editForm.week).format('MMM Do');
      const sRating = this.editForm.shanRating
        ? this.editForm.shanRating
        : '0';
      const cRating = this.editForm.cheRating
        ? this.editForm.cheRating
        : '0';
      const aRating = this.editForm.andhiRating
        ? this.editForm.andhiRating
        : '0';
      const avg = ((parseFloat(sRating) + parseFloat(cRating)
        + parseFloat(aRating)) / 3).toFixed(2);

      const payload = {
        week: weekFormatted,
        title: this.editForm.title,
        director: this.editForm.director,
        shanRating: sRating,
        cheRating: cRating,
        andhiRating: aRating,
        avgRating: avg,
      };
      this.updateMovie(payload, this.editForm.id);
    },
    updateMovie(payload, movieID) {
      const path = `http://localhost:5000/movies/${movieID}`;
      axios
        .put(path, payload)
        .then(() => {
          this.getMovies();
          this.message = 'Movie updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getMovies();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editMovieModal.hide();
      this.initForm();
      this.getMovies(); // why?
    },
    removeMovie(movieID) {
      const path = `http://localhost:5000/movies/${movieID}`;
      axios
        .delete(path)
        .then(() => {
          this.getMovies();
          this.message = 'Movie removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getMovies();
        });
    },
    onDeleteMovie(movie) {
      this.removeMovie(movie.id);
    },
  },
  created() {
    this.getMovies();
  },
};
</script>

<style>
.modal-backdrop {
  background-color: rgba(0, 0, 0, 0.75) !important;
}
.custom-range::-webkit-slider-thumb {
  background: #292b2c;
}
.custom-range::-webkit-slider-thumb:active {
  background-color: gray;
}
span.range-value-color {
  font-weight: 700;
}

.m-a {
  margin: auto;
}
</style>
