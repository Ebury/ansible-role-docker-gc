ansible-role-docker-gc
=========

Install and configure [docker-gc](https://github.com/spotify/docker-gc).

Role Variables
--------------

- `docker_gc_version` Git commit SHA1 from [docker-gc](https://github.com/spotify/docker-gc).

Dependencies
------------

- [geerlingguy.docker](https://github.com/geerlingguy/ansible-role-docker)

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: jenkins
      become: true
      become_method: sudo
      roles:
         - ebury.docker-gc

License
-------

BSD

Author Information
------------------

[Ebury](https://labs.ebury.rocks) Infrastructure Operations

