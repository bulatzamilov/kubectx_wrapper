# kubectx wrapper
kubectx cli tool with dialogue option.
Eventually you will have many contextes in your kubeconfig so kubectx becomes hard to use. This wrapper offers the dialogue with numbered contextes, so you need to pick the context you want to use by entering the corresponded number.

## Prerequisites
You need to have kubectx tool installed (https://github.com/ahmetb/kubectx) and accessible it from PATH.
Also, Python 3.6+ required

## Usage
Make sure you may run script granting executable bit to it by `chmod +x kubectx_dialogue.py`.
Then run it with `./kubectx_dialogue.py`

You may link it to eg /usr/local/bin/kubectx_wrapper and then check if this is in your PATH by `which kubectx_wrapper` but please don't rename it to kubectx because it will conflict with the existing kubectx tool. You may rename it to eg kctx.
When you link it to /usr/local/bin/kubectx_wrapper and /usr/local/bin is in your path you may just run kubectx_wrapper command

## Help
You run kubectx_wrapper, choose the context you want to switch to by entering its number. Voila~ you have changed current context

```
~/local/devops/kubectx_wrapper on  main!
$ kubectx -c
error: current-context is not set

~/local/devops/kubectx_wrapper on  main!
$ kctx
Current context is not set
1: test1
2: test2
3: docker-desktop
Please enter the number of corresponding context to switch to: 3
Switched to context "docker-desktop".

~/local/devops/kubectx_wrapper on  main!
$ kubectx -c
docker-desktop
```
