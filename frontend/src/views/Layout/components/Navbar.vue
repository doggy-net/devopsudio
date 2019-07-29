<template>
  <div>
    <div :class="logoClasses"></div>
    <el-menu mode="horizontal" router :default-active="baseRoute" class="float-left">
      <el-button @click="toggleSidebar" type="text" class="el-menu-button float-left">
        <icon icon-class="menu"/>
      </el-button>
      <el-menu-item index="/ops">
        <icon icon-class="operation"/>
        <span slot="title">{{ $t("message.operations") }}</span>
      </el-menu-item>
      <el-menu-item index="/dev">
        <icon icon-class="dev"/>
        <span slot="title">{{ $t("message.development") }}</span>
      </el-menu-item>
      <el-menu-item index="/admin">
        <icon icon-class="admin"/>
        <span slot="title">{{ $t("message.admin") }}</span>
      </el-menu-item>
    </el-menu>
    <div class="float-right">
      <el-popover placement="top-start" trigger="click">
        <el-tabs>
          <el-tab-pane label="Message">
            <el-collapse>
              <el-collapse-item title="一致性 Consistency" name="1">
                <div>与现实生活一致：与现实生活的流程、逻辑保持一致，遵循用户习惯的语言和概念；</div>
                <div>在界面中一致：所有的元素和结构需保持一致，比如：设计样式、图标和文本、元素的位置等。</div>
              </el-collapse-item>
              <el-collapse-item title="反馈 Feedback" name="2">
                <div>控制反馈：通过界面样式和交互动效让用户可以清晰的感知自己的操作；</div>
                <div>页面反馈：操作后，通过页面元素的变化清晰地展现当前状态。</div>
              </el-collapse-item>
              <el-collapse-item title="效率 Efficiency" name="3">
                <div>简化流程：设计简洁直观的操作流程；</div>
                <div>清晰明确：语言表达清晰且表意明确，让用户快速理解进而作出决策；</div>
                <div>帮助用户识别：界面简单直白，让用户快速识别而非回忆，减少用户记忆负担。</div>
              </el-collapse-item>
              <el-collapse-item title="可控 Controllability" name="4">
                <div>用户决策：根据场景可给予用户操作建议或安全提示，但不能代替用户进行决策；</div>
                <div>结果可控：用户可以自由的进行操作，包括撤销、回退和终止当前操作等。</div>
              </el-collapse-item>
            </el-collapse>
          </el-tab-pane>
          <el-tab-pane label="Alert">
            <el-collapse>
              <el-collapse-item title="一致性 Consistency" name="1">
                <div>与现实生活一致：与现实生活的流程、逻辑保持一致，遵循用户习惯的语言和概念；</div>
                <div>在界面中一致：所有的元素和结构需保持一致，比如：设计样式、图标和文本、元素的位置等。</div>
              </el-collapse-item>
              <el-collapse-item title="反馈 Feedback" name="2">
                <div>控制反馈：通过界面样式和交互动效让用户可以清晰的感知自己的操作；</div>
                <div>页面反馈：操作后，通过页面元素的变化清晰地展现当前状态。</div>
              </el-collapse-item>
              <el-collapse-item title="效率 Efficiency" name="3">
                <div>简化流程：设计简洁直观的操作流程；</div>
                <div>清晰明确：语言表达清晰且表意明确，让用户快速理解进而作出决策；</div>
                <div>帮助用户识别：界面简单直白，让用户快速识别而非回忆，减少用户记忆负担。</div>
              </el-collapse-item>
              <el-collapse-item title="可控 Controllability" name="4">
                <div>用户决策：根据场景可给予用户操作建议或安全提示，但不能代替用户进行决策；</div>
                <div>结果可控：用户可以自由的进行操作，包括撤销、回退和终止当前操作等。</div>
              </el-collapse-item>
            </el-collapse>
          </el-tab-pane>
          <el-tab-pane label="Notification">
            <el-collapse>
              <el-collapse-item title="一致性 Consistency" name="1">
                <div>与现实生活一致：与现实生活的流程、逻辑保持一致，遵循用户习惯的语言和概念；</div>
                <div>在界面中一致：所有的元素和结构需保持一致，比如：设计样式、图标和文本、元素的位置等。</div>
              </el-collapse-item>
              <el-collapse-item title="反馈 Feedback" name="2">
                <div>控制反馈：通过界面样式和交互动效让用户可以清晰的感知自己的操作；</div>
                <div>页面反馈：操作后，通过页面元素的变化清晰地展现当前状态。</div>
              </el-collapse-item>
              <el-collapse-item title="效率 Efficiency" name="3">
                <div>简化流程：设计简洁直观的操作流程；</div>
                <div>清晰明确：语言表达清晰且表意明确，让用户快速理解进而作出决策；</div>
                <div>帮助用户识别：界面简单直白，让用户快速识别而非回忆，减少用户记忆负担。</div>
              </el-collapse-item>
              <el-collapse-item title="可控 Controllability" name="4">
                <div>用户决策：根据场景可给予用户操作建议或安全提示，但不能代替用户进行决策；</div>
                <div>结果可控：用户可以自由的进行操作，包括撤销、回退和终止当前操作等。</div>
              </el-collapse-item>
            </el-collapse>
          </el-tab-pane>
        </el-tabs>
        <el-button type="text" slot="reference" class="el-menu-button">
          <el-badge :value="300" :max="99">
            <icon icon-class="message"/>
          </el-badge>
        </el-button>
      </el-popover>
      <el-dropdown trigger="click" @command="changeLang">
        <el-button type="text" class="el-menu-button">
          {{ curLang.label }}
        </el-button>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item
            v-for="item in langs"
            :key="item.value" :command="item" :disabled="curLang.value===item.value">
            {{ item.label }}
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <el-button type="text" @click="logout">
        {{ $t('message.logout') }}
      </el-button>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import { getBaseRoute } from '@/utils/path'
export default {
  name: 'Navbar',
  data () {
    return {
      langs: [{
        value: 'en',
        label: 'English'
      }, {
        value: 'zh-chs',
        label: '简体中文'
      }, {
        value: 'zh-cht',
        label: '繁體中文'
      }],
      curLang: {
        value: 'en',
        label: 'English'
      }
    }
  },
  computed: {
    ...mapState({
      isSidebarCollapsed: state => state.isSidebarCollapsed
    }),
    logoClasses() {
      if (this.isSidebarCollapsed) {
        return ['logo', 'logo--collapse'];
      }
      return ['logo'];
    },
    baseRoute() {
      return getBaseRoute(this.$route.path);
    }
  },
  methods: {
    ...mapMutations({
      toggleSidebar: 'toggleSidebar'
    }),
    changeLang(command) {
      this.curLang = command;
      this.$i18n.locale = this.curLang.value;
    },
    logout() {
      window.localStorage.removeItem('token')
      // this.$store.dispatch('LogOut').then(() => {
      //   location.reload()// In order to re-instantiate the vue-router object to avoid bugs
      // })
    }
  }
}
</script>

<style>
.logo {
  display: block;
  width: 200px;
  height: 60px;
  background-image: url("../../../assets/logo.png");
  float: left;
  transition: .3s width ease-in-out, .3s background-image ease-in-out;
}
.logo--collapse {
  width: 64px;
}
.el-menu-button {
  height: 60px;
  padding: 0 20px;
}
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  height: 100%;
}
.el-menu--collapse {
  height: 100%;
  width: 64px;
}
</style>
