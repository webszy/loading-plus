<template>
  <section class="seo" aria-labelledby="seo-title">
    <div class="container seo__inner">
      <h2 id="seo-title" class="section-title">Free loading animations for modern interfaces</h2>
      <div class="seo__body">
        <p>
          A loading animation is the part of an interface that explains a pause. It shows that a page, a request, or an action is still in progress, so the wait does not look like a broken screen. Spinners, dots, text treatments, progress bars, and skeletons are different shapes of that same idea.
        </p>

        <h3>Where loading states are used</h3>
        <p>
          They show up while a page opens, a route changes, a form submits, a file uploads, or a panel waits on data. A button can carry a small spinner. A card grid can hold skeletons. A longer task can use a bar. The useful choice depends on how much of the result is already known.
        </p>

        <h3>CSS loaders and GIF loaders</h3>
        <p>
          CSS loading animations are drawn with HTML and keyframes. They stay sharp at any size, can take on the colors of the surrounding UI, and can stop when someone prefers reduced motion. A GIF is a fixed sequence of image frames. It is easy to drop in, but the color, size, and timing are baked into the file, and it cannot follow a motion setting. CSS fits inside a product interface. A GIF is useful when the loader has to travel as a single image.
        </p>
        <p>
          The loaders in this collection are CSS animations. They loop in the browser and do not depend on image files.
        </p>

        <h3>What skeleton loading is for</h3>
        <p>
          A skeleton loader reserves the shape of content that has not arrived yet: lines for text, blocks for media, rows for lists. People can see how the page is organized before the data appears, which is easier to follow than an empty region with one spinner in the middle.
        </p>

        <h3>When to use an indeterminate progress bar</h3>
        <p>
          Use an indeterminate progress bar when work has started and the interface cannot honestly say how much is left. The moving bar shows activity without inventing a percentage. When the completed amount is known, a determinate bar should display that value instead.
        </p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.seo {
  padding: 8px 0 72px;
}

.seo__inner {
  max-width: 760px;
}

.seo__body {
  margin-top: 18px;
}

.seo__body h3 {
  margin-top: 28px;
  font-size: 18px;
  line-height: 1.3;
}

.seo__body p {
  margin-top: 8px;
  font-size: 16px;
  line-height: 1.7;
}

.seo__body h3 + p,
.seo__body p + p {
  margin-top: 8px;
}
</style>
