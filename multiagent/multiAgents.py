var gitlet = module.exports = {

  // **init()** initializes the current directory as a new repository.
  init: function(opts) {

    // Abort if already a repository.
    if (files.inRepo()) { return; }

    opts = opts || {};

    // Create a JS object that mirrors the Git basic directory
    // structure.
    var gitletStructure = {
      HEAD: "ref: refs/heads/master\n",

      // If `--bare` was passed, write to the Git config indicating
      // that the repository is bare.  If `--bare` was not passed,
      // write to the Git config saying the repository is not bare.
      config: config.objToStr({ core: { "": { bare: opts.bare === true }}}),

      objects: {},
      refs: {
        heads: {},
      }
    };
