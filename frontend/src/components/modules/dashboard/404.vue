<template>
    <div class="content-wrapper">
        <!-- Content Header (Page header) -->
        <section class="content-header">
            <h1>
                404 Error Page
            </h1>
            <ol class="breadcrumb">
                <li><a href="#"><i class="fa fa-dashboard"></i> Home</a></li>
                <li><a href="#">Examples</a></li>
                <li class="active">404 error</li>
            </ol>
        </section>
        <main class="wrapper-404">
            <div class="error-404">
                <div class="error-number"><span>4</span><span><img class="icon has-animation" src="https://image.flaticon.com/icons/svg/179/179595.svg" alt=""/></span><span>4</span></div>
                <h1> <vue-typer
  :text='["Oops! Page not found","We could not find the page you were looking for", "Meanwhile", "you may return to dashboard", "or try using the search form."]'
  :repeat='Infinity'
  :shuffle='false'
  initial-action='typing'
  :pre-type-delay='70'
  :type-delay='70'
  :pre-erase-delay='2000'
  :erase-delay='250'
  erase-style='clear'
  :erase-on-complete='false'
  caret-animation='solid'
></vue-typer></h1> </div>
        </main>
        <div class="moon"></div>
    </div>
</template>
<script>
export default {
  name: 'NotFound'
}
</script>
