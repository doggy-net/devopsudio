<template>
  <el-main>
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
    <el-progress :percentage="percentage" :status="state"></el-progress>
    <el-table :data="ipData">
      <el-table-column prop="ip" :label="$t('ui.ip')" width="180"/>
      <el-table-column prop="hostname" :label="$t('ui.hostname')"/>
    </el-table>
  </el-main>
</template>

<script>
import { startDiscovery, stopDiscovery, getDiscoveryStatus } from '@/api/discovery'
import AsyncButton from '@/components/AsyncButton'
import { validateIp } from '@/utils/ip'

export default {
  name: 'Discovery',
  components: {
    AsyncButton,
  },
  data() {
    function validateIps(ips) {
      try {
        const ipList = ips.split(";");
        for (const ipitem of ipList) {
          const ipstrList = ipitem.split('-')
          if (ipstrList.length > 1) {
            const ipstr1 = ipstrList[0];
            const ipstr2 = ipstrList[1];
            let ipwords1 = ipstr1.split('.');
            let ipwords2 = ipstr2.split('.');
            for (let index of [0, 1, 2, 3]) {
              ipwords1[index] = parseInt(ipwords1[index]);
              ipwords2[index] = parseInt(ipwords2[index]);
            }
            if (ipwords1 > ipwords2) {
              return false;
            }
            if (!validateIp(ipstr1)) {
              return false;
            }
            if (!validateIp(ipstr2)) {
              return false;
            }
          } else {
            const ipstr = ipstrList[0];
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
      loading: true,
      percentage: 0,
      state: null,
      ipData: [],
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
          this.$refs['commandButton'].loading = true;
          startDiscovery(this.discoveryForm)
            .then(() => {
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
            .catch(error => {
              this.$message({
                message: this.$t('message.discoveryFormStartedFailed') + ': ' + error,
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
      this.$refs['commandButton'].loading = true;
      stopDiscovery()
        .then(() => {
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
        .catch(error => {
          this.$message({
            message: this.$t('message.discoveryFormStoppedFailed') + ': ' + error,
            type: 'error',
            showClose: true,
            duration: 5 * 1000,
          });
          this.$refs['commandButton'].loading = false;
        });
    },
    initUpdate() {
      this.updateState();
      this.updateUI();
    },
    updateState() {
      getDiscoveryStatus()
        .then(response => {
          this.updateUI(response);
        })
        .catch(error => {
          this.updateUI(null, error);
        });
    },
    updateUI(response, error) {
      if (error) {
        this.state = 'exception';
        this.$refs['commandButton'].loading = false;
        this.$refs['commandButton'].state = 'normal';
        this.stopUpdateTimer();
        return;
      }
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
    },
    startUpdateTimer() {
      this.updateTimer = setInterval(this.updateState, 3 * 1000);
    },
    stopUpdateTimer() {
      clearInterval(this.updateTimer);
    }
  }
}
</script>
