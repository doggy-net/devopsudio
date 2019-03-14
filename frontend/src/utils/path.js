// translate router.meta.title, be used in breadcrumb sidebar tagsview
export function getBaseRoute(routePath) {
  return '/' + routePath.split('/')[1];
}
