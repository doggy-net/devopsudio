<template>
  <el-main>
    <div class="email-form">
      <el-form ref="form" :model="emailSettings" label-width="150px">
        <el-form-item :label="$t('ui.smtpServer')">
          <el-input v-model="emailSettings.smtp"></el-input>
        </el-form-item>
        <el-form-item :label="$t('ui.port')">
          <el-input v-model="emailSettings.port"></el-input>
        </el-form-item>
        <el-form-item :label="$t('ui.authenType')">
          <el-select v-model="emailSettings.authenType" placeholder="">
            <el-option label="None" value="None"></el-option>
            <el-option label="SSL" value="SSL"></el-option>
            <el-option label="TLS" value="TLS"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item :label="$t('ui.username')">
          <el-input v-model="emailSettings.username"></el-input>
        </el-form-item>
        <el-form-item :label="$t('ui.password')">
          <el-input v-model="emailSettings.password"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">{{ $t('ui.save') }}</el-button>
          <el-button>{{ $t('ui.cancle') }}</el-button>
        </el-form-item>
      </el-form>
    </div>
  </el-main>
</template>

<script>
export default {
  name: 'Email',
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
    }
  }
}
</script>

<style scoped>
.email-form {
  margin: 0px auto 0px auto;
  width: 600px;
}
</style>
