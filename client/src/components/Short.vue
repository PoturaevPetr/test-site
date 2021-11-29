<template>
  <div class="container" style='height:100%'>
    <div>
      <div class="col-sm-10" style="height: auto;">
        <h1>Provide a link to shorten</h1>
        <hr>
        <alert :message="message" v-if="showMessage" style="color: red"></alert>
        <input type="form-url-input" name="text" v-model="addUrlForm.url" required placeholder="Enter URL" style="border-radius: 25px;"></input>
        <button type="button" class="btn btn-success btn-sm" @click="onSubmit" style="border-radius: 20px;">Shorted</button>
        <br><br>
        <td v-for="(keys, index) in urls" :key="index">
          <table class="table" style="width:100%; border-radius: 25px;  color: rgb(0, 4, 69); background-color: white; table-layout: fixed;">
            <tbody>
              <tr>URL</tr>
              <td style="width: 100%; overflow: auto; white-space: nowrap;"><a :href='keys.url'>{{ keys.url }}</a></td>
              <tr>HASH</tr>
              <td style="width: 100%; overflow: auto; white-space: nowrap;"><a :href="keys.url">{{ keys.hash }}</a></td>
            </tbody>
          </table>
          <button type="button" class="btn btn-success btn-sm" @click="copyToClipboard(keys.url)" style="border-radius: 25px;">Copy</button>
        </td>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert';



export default {
  data() {
    return {
      urls: [],
      addUrlForm: {
        url: '',
        hash: '',
      },
      showMessage: false,
      message: '',
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getURL() {
      const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.urls = res.data.urls;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addURL(payload) {
      const path = 'http://localhost:5000/books';
      axios.post(path, payload)
        .then(() => {
          this.getURL();
          this.message = 'URL Shorted';
          this.showMessage = true;
        })
        .catch((error) => {
          console.log(error);
          this.getURL();
        });
    },
    initForm() {
      this.addUrlForm.url = '';
      this.addUrlForm.hash = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        url: this.addUrlForm.url,
        hash: this.addUrlForm.hash,
      };
      this.addURL(payload);
      this.initForm();
    },
    copyToClipboard(text) {
      this.message = 'Link copied'
      navigator.clipboard.readText()
      .then(text => {
        this.copyText = text;
      })
      .catch(err => {
        console.log('Something went wrong', err);
      });
    },
  },
  created() {
    this.getURL();
  },
};
</script>