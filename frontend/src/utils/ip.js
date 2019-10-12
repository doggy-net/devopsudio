export function validateIp(ip)
{
  if (/^\s*(?:(25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)(?:\/(3[0-2]|[12]?[0-9]))?\s*$/.test(ip))
  {
    return true;
  }
  return false;
}
