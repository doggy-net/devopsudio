<template>
  <div class="email-form">
    <el-form ref="form" :model="emailSettings" label-width="150px">
      <el-form-item :label="$t('message.smtpServer')">
        <el-input v-model="emailSettings.smtp"></el-input>
      </el-form-item>
      <el-form-item :label="$t('message.port')">
        <el-input v-model="emailSettings.port"></el-input>
      </el-form-item>
      <el-form-item :label="$t('message.authenType')">
        <el-select v-model="emailSettings.authenType" placeholder="">
          <el-option label="None" value="None"></el-option>
          <el-option label="SSL" value="SSL"></el-option>
          <el-option label="TLS" value="TLS"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item :label="$t('message.username')">
        <el-input v-model="emailSettings.username"></el-input>
      </el-form-item>
      <el-form-item :label="$t('message.password')">
        <el-input v-model="emailSettings.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">{{ $t('message.save') }}</el-button>
        <el-button>{{ $t('message.cancle') }}</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'User',
  data() {
    return {
      emailSettings: {
        smtp: '',
        port: '',
        authenType: [],
        username: '',
        password: ''
      }
    }
  },
  methods: {
    onSubmit() {
      console.log(11, this.$t('message'));
    }
  }
}
</script>

<style>
.email-form {
  margin: 20px auto 0px auto;
  width: 600px;
}
</style>
