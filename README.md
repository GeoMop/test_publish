# test_publish
Test actions for publisihing releases.


# How to make a release?

TODO:
- fix tox fr py35, py37
- action for publishing a release on tagged version
  - GITHUB release - manual ?? 
  - PYPI release
  - test on test_publish repo
  


    On Bacula, copy publish directory x.y.z to x.y.z_release.
    Convert CHANGES.md and README.md to html Jekyll files: make web-content
    Update the web: main.js, features, changes, readme
    Check that all links work.
    Upload to repository (publish)
    Create release tag, eg. for release 1.8.2 (within 1.8.2 branch):

git tag -a release_1.8.2 -m "Release 1.8.2"
git push origin release_1.8.2

0. Repository preparation:
   - check that master tests are green
   - update documentation, at least README.md files for subpackages
     (detailed doc should be mantained continuously before merge to master)
   - update CHANGES.md
   

1. Determine the release version number: major.minor.patch
   - Major for backward incompatible changes, changes in API.
   - Minor for backward compatible changes, no changes in API, possible slight changes in numerical results.
   - Patch for fixes, no substantial new features.
   Modify the VERSION file.

2. Make a tag, e.g. 
  
      git "v0.1.0":

