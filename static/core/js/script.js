document.addEventListener('DOMContentLoaded', function () {

  /* ---------- Mobile Navigation Toggle ---------- */
  const navToggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      navLinks.classList.toggle('open');
    });

    // Close menu when a link is clicked (mobile UX)
    navLinks.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        navLinks.classList.remove('open');
      });
    });
  }

  /* ---------- Highlight Active Nav Link ---------- */
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-links a').forEach(function (link) {
    const linkPath = new URL(link.href).pathname;
    if (linkPath === currentPath) {
      link.classList.add('active');
    }
  });

  /* ---------- Auto-dismiss Alert Messages ---------- */
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(function (alert) {
    setTimeout(function () {
      alert.style.transition = 'opacity 0.5s ease';
      alert.style.opacity = '0';
      setTimeout(function () { alert.remove(); }, 500);
    }, 6000);
  });

  /* ---------- Simple Client-Side Contact Form Validation ---------- */
  const contactForm = document.querySelector('#contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      const name = contactForm.querySelector('#id_name');
      const email = contactForm.querySelector('#id_email');
      const message = contactForm.querySelector('#id_message');
      let hasError = false;

      [name, email, message].forEach(function (field) {
        if (field && field.value.trim() === '') {
          field.style.borderColor = '#c0392b';
          hasError = true;
        } else if (field) {
          field.style.borderColor = '';
        }
      });

      if (email && email.value.trim() !== '') {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email.value.trim())) {
          email.style.borderColor = '#c0392b';
          hasError = true;
        }
      }

      if (hasError) {
        e.preventDefault();
      } else {
        e.preventDefault();
        
        const nameVal = name ? name.value.trim() : '';
        const emailVal = email ? email.value.trim() : '';
        const phone = contactForm.querySelector('#id_phone');
        const phoneVal = phone ? phone.value.trim() : '';
        const subject = contactForm.querySelector('#id_subject');
        const subjectVal = subject ? subject.value.trim() : '';
        const messageVal = message ? message.value.trim() : '';
        
        const whatsappNumber = "919994256650";
        const whatsappText = `Hello AMS Tea Traders,\n\nI would like to send a message:\nName: ${nameVal}\nEmail: ${emailVal}\nPhone: ${phoneVal || 'N/A'}\nSubject: ${subjectVal || 'N/A'}\nMessage: ${messageVal}`;
        
        const encodedText = encodeURIComponent(whatsappText);
        const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${encodedText}`;
        
        window.open(whatsappUrl, '_blank');
        contactForm.reset();
      }
    });
  }

  /* ---------- Product Category Filter (Products page) ---------- */
  const filterLinks = document.querySelectorAll('.filter-bar a');
  filterLinks.forEach(function (link) {
    const linkURL = new URL(link.href);
    const currentURL = new URL(window.location.href);
    if (linkURL.search === currentURL.search) {
      link.classList.add('active');
    }
  });

  /* ---------- Scroll-to-top on logo click already handled by href ---------- */

  /* ---------- Simple fade-in on scroll for cards ---------- */
  const revealItems = document.querySelectorAll('.card, .gallery-item, .value-item, .stat-box');
  if ('IntersectionObserver' in window && revealItems.length) {
    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    revealItems.forEach(function (item) {
      item.style.opacity = '0';
      item.style.transform = 'translateY(16px)';
      item.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      observer.observe(item);
    });
  }

  /* ---------- Current Year in Footer ---------- */
  const yearEl = document.querySelector('#footer-year');
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

});
