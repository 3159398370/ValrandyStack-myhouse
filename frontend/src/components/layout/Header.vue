<template>
  <header class="header">
    <div class="container">
      <div class="header-content">
        <div class="logo">
          <router-link to="/">
            <h1>ValrandyStack</h1>
          </router-link>
        </div>

        <nav class="nav-desktop" :class="{ 'active': isMenuActive }">
          <ul>
            <li v-for="item in navItems" :key="item.path">
              <router-link :to="item.path" :class="{ 'active': isActive(item.path) }">
                {{ item.name }}
              </router-link>
            </li>
          </ul>
        </nav>

        <div class="menu-toggle" @click="toggleMenu">
          <div class="bar" :class="{ 'animate': isMenuActive }"></div>
          <div class="bar" :class="{ 'animate': isMenuActive }"></div>
          <div class="bar" :class="{ 'animate': isMenuActive }"></div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      isMenuActive: false,
      navItems: [
        { name: '首页', path: '/' },
        { name: '作品集', path: '/projects' },
        { name: '代码仓库', path: '/repositories' },
        { name: '创意实验室', path: '/creative-lab' },
        { name: '关于我', path: '/about' },
      ],
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuActive = !this.isMenuActive;
      document.body.classList.toggle('menu-open');
    },
    isActive(path) {
      return this.$route.path === path || this.$route.path.startsWith(`${path}/`);
    },
    closeMenu() {
      if (this.isMenuActive) {
        this.isMenuActive = false;
        document.body.classList.remove('menu-open');
      }
    },
  },
  watch: {
    $route() {
      this.closeMenu();
    },
  },
};
</script>

<style scoped>
.header {
  background-color: #fff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 0;
}

.logo {
  display: flex;
  align-items: center;
}

.logo a {
  text-decoration: none;
  color: inherit;
}

.logo h1 {
  font-size: 1.8rem;
  font-weight: 700;
  color: #42b983;
  margin: 0;
  transition: color 0.3s ease;
}

.logo a:hover h1 {
  color: #369970;
}

.nav-desktop ul {
  display: flex;
  gap: 30px;
}

.nav-desktop a {
  color: #2c3e50;
  font-weight: 600;
  position: relative;
  padding-bottom: 5px;
}

.nav-desktop a:hover,
.nav-desktop a.active {
  color: #42b983;
}

.nav-desktop a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background-color: #42b983;
  transition: width 0.3s ease;
}

.nav-desktop a:hover::after,
.nav-desktop a.active::after {
  width: 100%;
}

.menu-toggle {
  display: none;
  flex-direction: column;
  justify-content: space-between;
  width: 30px;
  height: 21px;
  cursor: pointer;
}

.bar {
  height: 3px;
  width: 100%;
  background-color: #2c3e50;
  border-radius: 3px;
  transition: all 0.3s ease;
}

.bar.animate:nth-child(1) {
  transform: translateY(9px) rotate(45deg);
}

.bar.animate:nth-child(2) {
  opacity: 0;
}

.bar.animate:nth-child(3) {
  transform: translateY(-9px) rotate(-45deg);
}

@media (max-width: 768px) {
  .menu-toggle {
    display: flex;
  }

  .nav-desktop {
    position: fixed;
    top: 70px;
    left: 0;
    width: 100%;
    height: 0;
    background-color: #fff;
    overflow: hidden;
    transition: height 0.3s ease;
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  }

  .nav-desktop.active {
    height: calc(100vh - 70px);
  }

  .nav-desktop ul {
    flex-direction: column;
    padding: 20px;
    gap: 20px;
  }

  .nav-desktop a {
    display: block;
    padding: 10px 0;
    font-size: 1.2rem;
  }
}
</style>
