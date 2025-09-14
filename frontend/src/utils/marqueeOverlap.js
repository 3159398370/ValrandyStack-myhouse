// 跑马灯重叠隐藏效果工具函数

/**
 * 检测两个元素是否重叠
 * @param {HTMLElement} elem1 
 * @param {HTMLElement} elem2 
 * @returns {boolean}
 */
export function checkOverlap(elem1, elem2) {
  if (!elem1 || !elem2) return false;
  
  const rect1 = elem1.getBoundingClientRect();
  const rect2 = elem2.getBoundingClientRect();
  
  return !(rect1.right < rect2.left || 
           rect1.left > rect2.right || 
           rect1.bottom < rect2.top || 
           rect1.top > rect2.bottom);
}

/**
 * 隐藏跑马灯效果
 * @param {HTMLElement} element 
 * @param {boolean} hide 
 */
export function hideMarqueeEffect(element, hide = true) {
  if (!element) return;
  
  const classes = ['hide-marquee-glow', 'marquee-overlay-hidden'];
  
  if (hide) {
    element.classList.add(...classes);
  } else {
    element.classList.remove(...classes);
  }
}

/**
 * 获取与指定元素重叠的所有元素
 * @param {HTMLElement} targetElement 
 * @param {string} selector - 要检查的元素选择器
 * @returns {HTMLElement[]}
 */
export function getOverlappingElements(targetElement, selector = '*') {
  if (!targetElement) return [];
  
  const targetRect = targetElement.getBoundingClientRect();
  const elements = document.querySelectorAll(selector);
  
  return Array.from(elements).filter(element => {
    if (element === targetElement || !element.offsetParent) return false;
    
    const elementRect = element.getBoundingClientRect();
    
    return !(targetRect.right < elementRect.left || 
             targetRect.left > elementRect.right || 
             targetRect.bottom < elementRect.top || 
             targetRect.top > elementRect.bottom);
  });
}

/**
 * 防抖函数
 * @param {Function} func 
 * @param {number} wait 
 * @returns {Function}
 */
export function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func.apply(this, args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

/**
 * 自动检测并应用重叠隐藏效果
 * @param {string} marqueeSelector - 跑马灯选择器
 * @param {string} overlapSelector - 要检查重叠的元素选择器
 */
export function autoHideMarqueeOnOverlap(marqueeSelector = '.neon-marquee-demo', overlapSelector = '*') {
  const marqueeElements = document.querySelectorAll(marqueeSelector);
  
  const applyHideEffect = () => {
    marqueeElements.forEach(marquee => {
      const overlappingElements = getOverlappingElements(marquee, overlapSelector);
      
      if (overlappingElements.length > 0) {
        hideMarqueeEffect(marquee, true);
      } else {
        hideMarqueeEffect(marquee, false);
      }
    });
  };
  
  // 初始应用
  setTimeout(applyHideEffect, 100);
  
  // 监听事件
  const debouncedApply = debounce(applyHideEffect, 100);
  window.addEventListener('resize', debouncedApply);
  window.addEventListener('scroll', debouncedApply);
  
  // 返回清理函数
  return () => {
    window.removeEventListener('resize', debouncedApply);
    window.removeEventListener('scroll', debouncedApply);
  };
}

/**
 * 使用示例：
 * 
 * // 在Vue组件中使用
 * import { autoHideMarqueeOnOverlap, checkOverlap, hideMarqueeEffect } from '@/utils/marqueeOverlap';
 * 
 * mounted() {
 *   this.cleanup = autoHideMarqueeOnOverlap('.my-marquee', '.overlap-check');
 * },
 * 
 * beforeUnmount() {
 *   if (this.cleanup) this.cleanup();
 * }
 */