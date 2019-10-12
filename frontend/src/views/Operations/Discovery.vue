<template>
  <div style="padding: 20px">
    <el-form :model="discoveryForm" :rules="rules" ref="discoveryForm">
      <el-form-item prop="ips">
        <el-input autofocus v-model="discoveryForm.ips" style="width: 400px"
          placeholder="e.g. 10.0.0.1; 172.16.0.1-172.16.0.100; 192.168.0.0/24"/>
        <async-button style="margin-left: 10px" ref="commandButton"
          @init-state="updateState" @normal-click="handleStart" @danger-click="handleStop"
          normal-text="ui.startDiscovery" normal-loading-text="ui.starting"
          danger-text="ui.stop" danger-loading-text="ui.stopping">
        </async-button>
       </el-form-item>
    </el-form>
    <el-progress type="circle" :percentage="percentage" :status="state"></el-progress>
    <log-viewer :logs="logs"/>
  </div>
</template>

<script>
import { Message, MessageBox } from 'element-ui'
import AsyncButton from '@/components/AsyncButton'
import LogViewer from '@/components/LogViewer'
import { startDiscovery, stopDiscovery, getDiscoveryStatus } from '@/api/discovery'
import { validateIp } from '@/utils/ip'

export default {
  name: 'Discovery',
  components: {
    AsyncButton,
    LogViewer,
  },
  data() {
    function validateIps(ips)
    {
      try {
        const ipList = ips.split(";");
        for (const ipitem of ipList) {
          for (const ipstr of ipitem.split('-')) {
            if (!validateIp(ipstr)) {
              return false;
            }
          }
        }
      } catch (error) {
        console.log(error);
        return false;
      }
      return true;
    }
    var checkIps = (rule, value, callback) => {
      if (rule.required && !value) {
        return callback(new Error(this.$t('message.discoveryFormIpsEmpty')));
      }
      if (!validateIps(value)) {
        callback(new Error(this.$t('message.discoveryFormIpsInvalid')));
      } else {
        callback();
      }
    };
    return {
      discoveryForm: {
        ips: ''
      },
      rules: {
        ips: [
          {
            required: true,
            validator: checkIps,
            trigger: 'blur',
          }
        ]
      },
      discoveryButton: {
        loading: false,
        isStart: true,
      },
      percentage: 0,
      state: null,
      logs: [],
    }
  },
  created() {
    this.startUpdateTimer();
  },
  beforeDestroy () {
    this.stopUpdateTimer();
  },
  methods: {
    handleStart() {
      this.$refs['discoveryForm'].validate((valid) => {
        if (valid) {
          this.state = null;
          this.percentage = 0;
          startDiscovery(this.discoveryForm)
            .then(response => {
              this.$message({
                message: this.$t('message.discoveryFormStarted'),
                type: 'success',
                showClose: true,
                duration: 5 * 1000,
              });
              this.startUpdateTimer();
              this.$refs['commandButton'].loading = false;
              this.$refs['commandButton'].state = 'running';
            })
            .catch(err => {
              this.$message({
                message: this.$t('message.discoveryFormStartedFailed') + ': ' + err,
                type: 'error',
                showClose: true,
                duration: 5 * 1000,
              });
              this.$refs['commandButton'].loading = false;
              this.$refs['commandButton'].state = 'normal';
            });
        } else {
          return;
        }
      });
    },
    handleStop() {
      stopDiscovery()
        .then(response => {
          this.state = 'warning';
          this.$message({
            message: this.$t('message.discoveryFormStopped'),
            type: 'success',
            showClose: true,
            duration: 5 * 1000,
          });
          this.stopUpdateTimer();
          this.$refs['commandButton'].loading = false;
          this.$refs['commandButton'].state = 'normal';
        })
        .catch(err => {
          this.$message({
            message: this.$t('message.discoveryFormStoppedFailed') + ': ' + err,
            type: 'error',
            showClose: true,
            duration: 5 * 1000,
          });
          this.$refs['commandButton'].loading = false;
        });
    },
    updateState() {
      getDiscoveryStatus()
        .then(response => {
          if (response.state === 'SUCCESS') {
            this.$refs['commandButton'].state = 'normal';
            this.state = 'success';
            this.stopUpdateTimer();
          } else if (response.state === 'FAILED') {
            this.$refs['commandButton'].state = 'normal';
            this.state = 'warning';
            this.stopUpdateTimer();
          } else if (response.state === 'ERROR') {
            this.$refs['commandButton'].state = 'normal';
            this.state = 'exception';
            this.stopUpdateTimer();
          } else {
            this.state = null;
            this.$refs['commandButton'].state = 'running';
          }
          this.percentage = response.progress / response.total * 100;
          this.$refs['commandButton'].loading = false;
        })
        .catch(err => {
          this.state = 'exception';
          this.$refs['commandButton'].loading = false;
          this.$refs['commandButton'].state = 'normal';
        });
    },
    startUpdateTimer() {
      this.updateTimer = setInterval(this.updateState, 3 * 1000);
    },
    stopUpdateTimer() {
      clearInterval(this.updateTimer);
    },
  },
}
</script>
