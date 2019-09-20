<template>
  <div style="padding: 20px">
    <el-form :model="discoveryForm" :rules="rules" ref="discoveryForm">
      <el-form-item prop="ips">
        <el-input autofocus v-model="discoveryForm.ips" style="width: 400px"
          placeholder="e.g. 10.0.0.1; 172.16.0.1-172.16.0.100; 192.168.0.0/24"/>
        <el-button style="margin-left: 10px"
          @click="handleDiscovery" :loading="discoveryButton.loading"
          :type="discoveryButtonType">{{ $t(discoveryButtonText) }}</el-button>
       </el-form-item>
    </el-form>
    <el-button @click="refresh">Refresh</el-button>
    <log-viewer :logs="logs"/>
  </div>
</template>

<script>
import { MessageBox, Message } from 'element-ui'
import LogViewer from '@/components/LogViewer'
import { startDiscovery, getDiscoveryStatus } from '@/api/discovery'

export default {
  name: 'Discovery',
  components: {
    LogViewer
  },
  data() {
    function validateIp(ip)
    {
      if (/^\s*(?:(25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)(?:\/(3[0-2]|[12]?[0-9]))?\s*$/.test(ip))
      {
        return true;
      }
      return false;
    }
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
        ips: '192.168.0.101'
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
        text: '',
      },
      logs: [],
      taskId: '',
    }
  },
  computed:{
    discoveryButtonType() {
      return this.discoveryButton.isStart ? 'primary' : 'danger';
    },
    discoveryButtonText() {
      if (this.discoveryButton.isStart) {
        if (this.discoveryButton.loading) {
          return 'ui.starting'
        } else {
          return 'ui.startDiscovery'
        }
      } else {
        if (this.discoveryButton.loading) {
          return 'ui.stopping'
        } else {
          return 'ui.stop'
        }
      }
      return this.discoveryButton.isStart ? 'primary' : 'danger';
    }
  },
  created() {
    console.log('created');
  },
  beforeDestroy() {
    console.log('beforeDestroy');
  },
  methods: {
    handleDiscovery() {
      if (this.discoveryButton.isStart) {
        this.$refs['discoveryForm'].validate((valid) => {
          if (valid) {
            this.discoveryButton.loading = true;
            startDiscovery(this.discoveryForm)
            .then(response => {
              this.$message({
                message: this.$t('message.discoveryFormStarted'),
                type: 'success',
                showClose: true,
                duration: 5 * 1000,
              });
              this.discoveryButton.loading = false;
              this.discoveryButton.isStart = false;
              this.taskId = response['taskId'];
              console.log('bbb');
              console.log(this.taskId);
              // setInterval(function() {
              //   num++;
              //   var date = new Date();
              //   document.write(date.getMinutes() + ':' + date.getSeconds() + ':' + date.getMilliseconds() + '<br>');
              //   if (num > 10)
              //       clearInterval(i);
              // }, 1000);
            })
            .catch(err => {
              this.$message({
                message: this.$t('message.discoveryFormStartedFailed') + ': ' + err,
                type: 'error',
                showClose: true,
                duration: 5 * 1000,
              })
              this.discoveryButton.loading = false;
            });
          } else {
            return false;
          }
        });
      } else {
        this.discoveryButton.loading = true;
        this.discoveryButton.loading = false;
        this.discoveryButton.isStart = true;
      }
    },
    refresh() {
      console.log(this.taskId, 'refresh');
      if (!this.taskId) {
        return;
      }
      getDiscoveryStatus(this.taskId)
      .then(response => {
      })
      .catch(err => {
      });
    }
  }
}
</script>
