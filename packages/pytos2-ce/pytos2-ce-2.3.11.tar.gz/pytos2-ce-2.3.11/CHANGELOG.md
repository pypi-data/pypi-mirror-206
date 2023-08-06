# Changelog
All notable changes to this project will be documented in this file

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

## [2.3.11] - 2023-02-10
- BUGFIX: Correctly handle payloads for updated to RecordSets
- FEATURE: Scw.add_attachment() - Add file attchment to SecureChange
- Add Models:
  - GenericIgnoredInterface
  - GenericInterfaceCustomer
  - GenericRoute
  - GenericVpn
  - JoinCloud
  - GenericTransparentFirewall
  - GenericIgnoredInterface
  - GenericInterfaceCustomer
  - 
- Add: 
  - St.add_generic_route() - Add Generic Route
  - St.add_generic_routes() - Add multiple Generic Routes
  - St.get_generic_route() - Get Generic Route by id
  - St.get_generic_rotues() - Get Generic Routes
  - St.update_generic_route() - Update Generic Route
  - St.update_generic_routes() - Update Multiple Generic Routes
  - St.delete_generic_route() - Delete Generic Route by id 
  - St.delete_generic_routes() - Delete Generic Routes by device
  - St.add_generic_vpn() - Add Generic VPN
  - St.add_generic_vpns()  - Add Multiple Generic VPN
  - St.get_generic_vpn() - Get Generic VPN by id
  - St.get_generic_vpns() - Get Generic VPN by device
  - St.update_generic_vpn() - Update Generic VPN by id
  - St.update_generic_vpns() - Update Generic VPN by device
  - St.delete_generic_vpn() - Delete Generic VPN by id
  - St.delete_generic_vpns() - Delete Generic VPN by device
  - St.add_generic_transparent_firewalls() - Add Generic Transparent Firewalls
  - St.get_generic_transparent_firewalls() - Get Generic Transparent Firewalls by device
  - St.update_generic_transparent_firewalls() - Update Generic Transparent Firewalls
  - St.delete_generic_transparent_firewall() - Delete Transparent Firewall by id
  - St.add_generic_ignored_interfaces() - Add ignored interfaces
  - St.get_generic_ignored_interfaces() - Get ignored interfaces by device
  - St.delete_generic_ignored_interfaces() - Delete ignored interface by device
  - St.add_generic_interface_customer()  - Add Generic Interface Customer Tag
  - St.add_generic_interface_customers() - Add Multiple Generic Interface Customer Tags
  - St.get_generic_interface_customer() - Get Interface Customer Tag by device
  - St.get_generic_interface_customers() = Get Interface Customer Tags by device
  - St.update_generic_interface_customer()
  - St.update_generic_interface_customers()
  - St.delete_generic_interface_customer()
  - St.delete_generic_interface_customers()
  - St.add_join_cloud() - Add join cloud
  - St.get_join_cloud() - Get join clouds by id
  - St.update_join_cloud() - Update join cloud
  - St.delete_join_cloud() - Deletee join cloud

## [2.3.10] - 2022-10-31
- FEATURE: 
  - Scw.get_attachment() - Get attachment from SecureChange by file_id
  - St.add_generic_interface() - Add Generic Interface
  - St.add_generic_interfaces() - Add Multiple Generic Interfaces
  - St.get_generic_interface() - Get Generic Interface by id
  - St.get_generic_interfaces() - Get all generic interfaces by device
  - St.update_generic_interface() - Update generic interface by id
  - St.update_generic_interfaces() 
  - St.delete_generic_interface() - Delete generic Interface by id
  - St.delete_generic_interfaces()) - Delete generic Interfaces by device
  - 
- New Models:
  - Ticket.Attachment
  - GenericInterface

## [2.3.9] - 2022-10-26
### Added
- Additional test data and tests
- Tox configuration for testing
### Changed
- BUGFIX: Fix duplicate target issue for Fortimanager when using multiple policies
- BUGFIX: Handle miissing singleServiceDTO.class_name for some Aur object results
- BUGFIX: Correct model for bindable objects
- BUGFIX: Correct issue with policies when device is ASA
## [2.3.8] - 2022-08-03
### API Changes
- Adds `AnyNetworkObject` mapping for SecureChange network objects.

## [2.3.7] - 2022-08-03
### API Changes
- Adds `HostNetworkObjectWithInterfaces` mapping for SecureChange network objects.

## [2.3.6] - 2022-08-03
### Fixes
- Fixes mismapped `Instruction.sources` and `Instruction.destinations`

## [2.3.5] - 2022-08-02
### API Changes
- Adds an `AnyService` mapping for service objects in `SlimRule`.
- Adds `comment`, `version_id`, `referenced`, `type_on_device`, `negate`, and `match_for_any` to `ServiceObject`

## [2.3.4] - 2022-08-02
### API Changes
- Adds a CloneServerPolicyRequest mapping to pytos2.securechange.fields
- Changes mapping type for `ServerDecommissionRequest.servers` from `IPObject` to `Object`

## [2.3.3] - 2022-08-01
### Fixes
- Changes mapping type for `ServerDecommissionRequest.servers` from `IPObject` to `Object`
- Updates cache when user not found in Scw.get_user(...)
- Handles "localuser" XSI type properly.
### API Changes
- Re-type several fields in SCWParty and SCWUser.
- Adds update_cache: bool to Scw.get_user(...)

## [2.3.2] - 2022-07-29
### Fixes
- Moves instruction mappings around.

## [2.3.1] - 2022-07-12
### Fixes
- Combines designer.Rule and rule.SlimRule
### API Changes
- Deprecates `SlimRule.source_networks` in favor of `SlimRule.source_objects`
- Deprecates `SlimRule.destination_networks` in favor of `SlimRule.destination_objects`
- Deprecates `SlimRule.destination_services` in favor of `SlimRule.services`
- Deprecates `designer.Rule`

## [2.3.0] - 2022-07-08
### Fixes
- Adds missing fields to SlimRule mapping
### API Changes
- Adds `TicketHistory` mappings

## [2.3.0] - 2022-08-11
### Added
- Added license
- Documentation updates
### Changed
- BUGFIX: Desginer/Verifier syntax error.

## [2.2.1] - 2021-12-23
- First public release!
