#### On this page

  * [Create a merge request](#create-a-merge-request)
  * [Use merge request templates](#use-merge-request-templates)
  * [View merge requests](#view-merge-requests)
  * [Filter the list of merge requests](#filter-the-list-of-merge-requests)
  * [By environment or deployment date](#by-environment-or-deployment-date)
  * [Add changes to a merge request](#add-changes-to-a-merge-request)
  * [Assign a user to a merge request](#assign-a-user-to-a-merge-request)
  * [Merge a merge request](#merge-a-merge-request)
  * [Close a merge request](#close-a-merge-request)
  * [Delete the source branch on merge](#delete-the-source-branch-on-merge)
  * [Update merge requests when target branch merges](#update-merge-requests-when-target-branch-merges)
  * [Merge request workflows](#merge-request-workflows)
  * [Filter activity in a merge request](#filter-activity-in-a-merge-request)
  * [Resolve a thread](#resolve-a-thread)
  * [Move all unresolved threads in a merge request to an issue](#move-all-unresolved-threads-in-a-merge-request-to-an-issue)
  * [Move one unresolved thread in a merge request to an issue](#move-one-unresolved-thread-in-a-merge-request-to-an-issue)
  * [Prevent merge unless all threads are resolved](#prevent-merge-unless-all-threads-are-resolved)
  * [Automatically resolve threads in a merge request when they become outdated](#automatically-resolve-threads-in-a-merge-request-when-they-become-outdated)
  * [Move notifications and to-dos](#move-notifications-and-to-dos)
  * [Related topics](#related-topics)



# Merge requests[](#merge-requests "Permalink")

**Tier:** Free, Premium, Ultimate **Offering:** GitLab.com, Self-managed, GitLab Dedicated

**History**

  * Sidebar actions menu [changed](https://gitlab.com/gitlab-org/gitlab/-/issues/373757) to also move actions on issues, incidents, and epics in GitLab 16.0. 
  * [Generally available](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/127001) in GitLab 16.9. Feature flag `moved_mr_sidebar` removed. 



A merge request (MR) is a proposal to incorporate changes from a source branch to a target branch. 

When you open a merge request, you can visualize and collaborate on the changes before merge. Merge requests include: 

  * A description of the request. 
  * Code changes and inline code reviews. 
  * Information about CI/CD pipelines. 
  * A comment section for discussion threads. 
  * The list of commits. 



## Create a merge request[](#create-a-merge-request "Permalink")

Learn the various ways to [create a merge request](creating_merge_requests.html). 

### Use merge request templates[](#use-merge-request-templates "Permalink")

When you create a merge request, GitLab checks for the existence of a [description template](../description_templates.html) to add data to your merge request. GitLab checks these locations in order from 1 to 5, and applies the first template found to your merge request: 

Name | Project UIsetting | Group`default.md` | Instance`default.md` | Project`default.md` | No template   
---|---|---|---|---|---  
Standard commit message | 1 | 2 | 3 | 4 | 5   
Commit message with an [issue closing pattern](../issues/managing_issues.html#closing-issues-automatically) like `Closes #1234` | 1 | 2 | 3 | 4 | 5 *   
Branch name [prefixed with an issue ID](../repository/branches/index.html#prefix-branch-names-with-issue-numbers), like `1234-example` | 1 * | 2 * | 3 * | 4 * | 5 *   
  
note

Items marked with an asterisk (*) also append an [issue closing pattern](../issues/managing_issues.html#closing-issues-automatically).

## View merge requests[](#view-merge-requests "Permalink")

You can view merge requests for your project, group, or yourself. 

  * [Assigned to you](#)
  * [For a project](#)
  * [For all projects in a group](#)



To view all merge requests assigned to you, use the `Shift` + `m` [keyboard shortcut](../../shortcuts.html), or: 

  1. On the left sidebar, select **Search or go to**. 
  2. From the dropdown list, select **Merge requests assigned to me**. 



or: 

  1. On the left sidebar, select **Code > Merge requests** (). 
  2. From the dropdown list, select **Assigned**. 



To view all merge requests for a project: 

  1. On the left sidebar, select **Search or go to** and find your project. 
  2. Select **Code > Merge requests**. 



Or, to use a [keyboard shortcut](../../shortcuts.html), press `g` + `m`. 

To view merge requests for all projects in a group: 

  1. On the left sidebar, select **Search or go to** and find your group. 
  2. Select **Code > Merge requests**. 



If your group contains subgroups, this view also displays merge requests from the subgroup projects. 

## Filter the list of merge requests[](#filter-the-list-of-merge-requests "Permalink")

**History**

  * Filtering by `source-branch` [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/134555) in GitLab 16.6. 
  * Filtering by `merged-by` [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/140002) in GitLab 16.9. Available only when the feature flag `mr_merge_user_filter` is enabled. 
  * Filtering by `merged-by` [generally available](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/142666) in GitLab 17.0. Feature flag `mr_merge_user_filter` removed. 



To filter the list of merge requests: 

  1. On the left sidebar, select **Search or go to** and find your project. 
  2. Select **Code > Merge requests**. 
  3. Above the list of merge requests, select **Search or filter results**. 
  4. From the dropdown list, select the attribute you wish to filter by. Some examples: 
     * [**By environment or deployment date**](#by-environment-or-deployment-date). 
     * **ID** : Enter filter `#30` to return only merge request 30. 
     * User filters: Type (or select from the dropdown list) any of these filters to display a list of users: 
       * **Approved-By** , for merge requests already approved by a user. Premium and Ultimate only. 
       * **Approver** , for merge requests that this user is eligible to approve. (For more information, read about [Code owners](../codeowners/index.html)). Premium and Ultimate only. 
       * **Merged-By** , for merge requests merged by this user. 
       * **Reviewer** , for merge requests reviewed by this user. 
  5. Select or type the operator to use for filtering the attribute. The following operators are available: 
     * `=`: Is 
     * `!=`: Is not 
  6. Enter the text to filter the attribute by. You can filter some attributes by **None** or **Any**. 
  7. Repeat this process to filter by more attributes, joined by a logical `AND`. 
  8. Select a **Sort direction** , either for descending order, or for ascending order. 



### By environment or deployment date[](#by-environment-or-deployment-date "Permalink")

To filter merge requests by deployment data, such as the environment or a date, you can type (or select from the dropdown list) the following: 

  * Environment 
  * Deployed-before 
  * Deployed-after 



note

Projects using a [fast-forward merge method](methods/index.html#fast-forward-merge) do not return results, as this method does not create a merge commit.

When filtering by an environment, a dropdown list presents all environments that you can choose from. 

When filtering by `Deployed-before` or `Deployed-after`: 

  * The date refers to when the deployment to an environment (triggered by the merge commit) completed successfully. 
  * You must enter the deploy date manually. 
  * Deploy dates use the format `YYYY-MM-DD`. Wrap them in double quotes (`"`) if you want to specify both a date and time (`"YYYY-MM-DD HH:MM"`). 



## Add changes to a merge request[](#add-changes-to-a-merge-request "Permalink")

If you have permission to add changes to a merge request, you can add your changes to an existing merge request in several ways. These ways depend on the complexity of your change, and whether you need access to a development environment: 

  * [Edit changes in the Web IDE](../web_ide/index.html) in your browser with the `.` [keyboard shortcut](../../shortcuts.html). Use this browser-based method to edit multiple files, or if you are not comfortable with Git commands. You cannot run tests from the Web IDE. 
  * [Edit changes in Gitpod](../../../integration/gitpod.html#launch-gitpod-in-gitlab), if you need a fully-featured environment to both edit files, and run tests afterward. Gitpod supports running the [GitLab Development Kit (GDK)](https://gitlab.com/gitlab-org/gitlab-development-kit). To use Gitpod, you must [enable Gitpod in your user account](../../../integration/gitpod.html#enable-gitpod-in-your-user-preferences). 
  * [Push changes from the command line](../../../topics/git/commands.html), if you are familiar with Git and the command line. 



## Assign a user to a merge request[](#assign-a-user-to-a-merge-request "Permalink")

To assign the merge request to a user, use the `/assign @user` [quick action](../quick_actions.html#issues-merge-requests-and-epics) in a text area in a merge request, or: 

  1. On the left sidebar, select **Search or go to** and find your project. 
  2. Select **Code > Merge requests** and find your merge request. 
  3. On the right sidebar, expand the right sidebar and locate the **Assignees** section. 
  4. Select **Edit**. 
  5. Search for the user you want to assign, and select the user. GitLab Free allows one assignee per merge request, but GitLab Premium and GitLab Ultimate allow multiple assignees: 

[![Two assignees for merge requests sidebar](img/merge_request_assignees_v16_0.png)](img/merge_request_assignees_v16_0.png)




GitLab adds the merge request to the user’s **Assigned merge requests** page. 

## Merge a merge request[](#merge-a-merge-request "Permalink")

During the [merge request review process](reviews/index.html), reviewers provide feedback on your changes. When a reviewer is satisfied with the changes, they can enable [auto-merge](auto_merge.html), even if some merge checks are failing. After all merge checks pass, the merge request is automatically merged, without further action from you. 

Default merge permissions: 

  * The default branch, typically `main`, is protected. 
  * Only Maintainers and higher roles can merge into the default branch. 
  * Developers can merge any merge requests targeting non-protected branches. 



To determine if you have permission to merge a specific merge request, GitLab checks: 

  * Your [role in the project](../../permissions.html#roles). For example, Developer, Maintainer, or Owner. 
  * The [branch protections](../repository/branches/protected.html) of the target branch. 



## Close a merge request[](#close-a-merge-request "Permalink")

If you decide to permanently stop work on a merge request, close it rather than [deleting it](manage.html#delete-a-merge-request). 

Prerequisites: 

  * You must be the author or assignees of the merge request, or 
  * You must have the Developer, Maintainer, or Owner [roles](../../permissions.html) in a project. 



To close merge requests in the project: 

  1. On the left sidebar, select **Search or go to** and find your project. 
  2. Select **Code > Merge requests** and find your merge request. 
  3. Scroll to the comment box at the bottom of the page. 
  4. Following the comment box, select **Close merge request**. 



GitLab closes the merge request, but preserves records of the merge request, its comments, and any associated pipelines. 

### Delete the source branch on merge[](#delete-the-source-branch-on-merge "Permalink")

You can delete the source branch for a merge request: 

  * When you create a merge request, by selecting **Delete source branch when merge request accepted**. 
  * When you merge a merge request, if you have the Maintainer role, by selecting **Delete source branch**. 



An administrator can make this option the default in the project’s settings. 

The delete-branch action is performed by the user who sets auto-merge, or merges the merge request. If the user lacks the correct role, such as in a forked project, the source branch deletion fails. 

### Update merge requests when target branch merges[](#update-merge-requests-when-target-branch-merges "Permalink")

**Tier:** Free, Premium, Ultimate **Offering:** GitLab.com, Self-managed, GitLab Dedicated

Merge requests are often chained together, with one merge request depending on the code added or changed in another merge request. To support keeping individual merge requests small, GitLab can update up to four open merge requests when their target branch merges into `main`. For example: 

  * **Merge request 1** : merge `feature-alpha` into `main`. 
  * **Merge request 2** : merge `feature-beta` into `feature-alpha`. 



If these merge requests are open at the same time, and merge request 1 (`feature-alpha`) merges into `main`, GitLab updates the destination of merge request 2 from `feature-alpha` to `main`. 

Merge requests with interconnected content updates are usually handled in one of these ways: 

  * Merge request 1 merges into `main` first. Merge request 2 is then retargeted to `main`. 
  * Merge request 2 merges into `feature-alpha`. The updated merge request 1, which now contains the contents of `feature-alpha` and `feature-beta`, merges into `main`. 



This feature works only when a merge request is merged. Selecting **Remove source branch** after merging does not retarget open merge requests. This improvement is [proposed as a follow-up](https://gitlab.com/gitlab-org/gitlab/-/issues/321559). 

## Merge request workflows[](#merge-request-workflows "Permalink")

For a software developer working in a team: 

  1. You check out a new branch, and submit your changes through a merge request. 
  2. You gather feedback from your team. 
  3. You work on the implementation optimizing code with [Code Quality reports](../../../ci/testing/code_quality.html). 
  4. You verify your changes with [Unit test reports](../../../ci/testing/unit_test_reports.html) in GitLab CI/CD. 
  5. You avoid using dependencies whose license is not compatible with your project with [License approval policies](../../../user/compliance/license_approval_policies.html). 
  6. You request the [approval](approvals/index.html) from your manager. 
  7. Your manager: 
    1. Pushes a commit with their final review. 
    2. [Approves the merge request](approvals/index.html). 
    3. Sets it to [auto-merge](auto_merge.html) (formerly **Merge when pipeline succeeds**). 
  8. Your changes get deployed to production with [manual jobs](../../../ci/jobs/job_control.html#create-a-job-that-must-be-run-manually) for GitLab CI/CD. 
  9. Your implementations were successfully shipped to your customer. 



For a web developer writing a webpage for your company’s website: 

  1. You check out a new branch and submit a new page through a merge request. 
  2. You gather feedback from your reviewers. 
  3. You preview your changes with [review apps](../../../ci/review_apps/index.html). 
  4. You request your web designers for their implementation. 
  5. You request the [approval](approvals/index.html) from your manager. 
  6. After approval, GitLab: 
     * [Squashes](squash_and_merge.html) the commits. 
     * Merges the commit. 
     * [Deployed the changes to staging with GitLab Pages](https://about.gitlab.com/blog/2021/02/05/ci-deployment-and-environments/). 
  7. Your production team [cherry-picks](cherry_pick_changes.html) the merge commit into production. 



## Filter activity in a merge request[](#filter-activity-in-a-merge-request "Permalink")

**History**

  * [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/115383) in GitLab 15.11 [with a flag](../../../administration/feature_flags.html) named `mr_activity_filters`. Disabled by default. 
  * [Enabled on GitLab.com](https://gitlab.com/gitlab-org/gitlab/-/issues/387070) in GitLab 16.0. 
  * [Enabled on self-managed](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/126998) in GitLab 16.3 by default. 
  * [Generally available](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/132355) in GitLab 16.5. Feature flag `mr_activity_filters` removed. 
  * Filtering bot comments [introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/128473) in GitLab 16.9. 



To understand the history of a merge request, filter its activity feed to show you only the items that are relevant to you. 

  1. On the left sidebar, select **Search or go to** and find your project. 
  2. Select **Code > Merge requests**. 
  3. Select a merge request. 
  4. Scroll to **Activity**. 
  5. On the right side of the page, select **Activity filter** to show the filter options. If you’ve already selected filter options, this field shows a summary of your choices, like **Activity + 5 more**. 
  6. Select the types of activity you want to see. Options include: 

     * Assignees & Reviewers 
     * Approvals 
     * Comments (from bots) 
     * Comments (from users) 
     * Commits & branches 
     * Edits 
     * Labels 
     * Lock status 
     * Mentions 
     * Merge request status 
     * Tracking 
  7. Optional. Select **Sort** () to reverse the sort order. 



Your selection persists across all merge requests. You can also change the sort order by clicking the sort button on the right. 

## Resolve a thread[](#resolve-a-thread "Permalink")

When you want to finish a conversation in a merge request, [resolve a thread](../../discussions/index.html#resolve-a-thread). 

GitLab shows the number of unresolved threads in the top right corner of a merge request, like this: **7 unresolved threads**. 

### Move all unresolved threads in a merge request to an issue[](#move-all-unresolved-threads-in-a-merge-request-to-an-issue "Permalink")

If you have multiple unresolved threads in a merge request, you can create an issue to resolve them separately: 

  1. On the left sidebar, select **Search or go to** and find your project. 
  2. Select **Code > Merge requests** and find your merge request. 
  3. In the merge request, in the top right, find the **Unresolved threads** dropdown list, and select **Thread options** (). 
  4. Select **Resolve all with new issue**. 
  5. Fill out the fields in the new issue, and select **Create issue**. 



GitLab marks all threads as resolved, and adds a link from the merge request to the newly created issue. 

### Move one unresolved thread in a merge request to an issue[](#move-one-unresolved-thread-in-a-merge-request-to-an-issue "Permalink")

If you have one specific unresolved thread in a merge request, you can create an issue to resolve it separately: 

  1. On the left sidebar, select **Search or go to** and find your project. 
  2. Select **Code > Merge requests** and find your merge request. 
  3. In the merge request, find the thread you want to move. 
  4. Below the last reply to the thread, next to **Resolve thread** , select **Create issue to resolve thread** (). 
  5. Fill out the fields in the new issue, and select **Create issue**. 



GitLab marks the thread as resolved, and adds a link from the merge request to the newly created issue. 

### Prevent merge unless all threads are resolved[](#prevent-merge-unless-all-threads-are-resolved "Permalink")

You can prevent merge requests from merging while threads remain unresolved. When you enable this setting, the **Unresolved threads** counter in a merge request is shown in orange while at least one thread remains unresolved. 

  1. On the left sidebar, select **Search or go to** and find your project. 
  2. Select **Settings > Merge requests**. 
  3. In the **Merge checks** section, select the **All threads must be resolved** checkbox. 
  4. Select **Save changes**. 



### Automatically resolve threads in a merge request when they become outdated[](#automatically-resolve-threads-in-a-merge-request-when-they-become-outdated "Permalink")

You can set merge requests to automatically resolve threads when a new push changes the lines they describe. 

  1. On the left sidebar, select **Search or go to** and find your project. 
  2. Select **Settings > Merge requests**. 
  3. In the **Merge options** section, select **Automatically resolve merge request diff threads when they become outdated**. 
  4. Select **Save changes**. 



Threads are now resolved if a push makes a diff section outdated. Threads on lines that don’t change and top-level resolvable threads are not resolved. 

## Move notifications and to-dos[](#move-notifications-and-to-dos "Permalink")

**Tier:** Free, Premium, Ultimate **Offering:** Self-managed

**History**

  * [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/132678) in GitLab 16.5 [with a flag](../../../administration/feature_flags.html) named `notifications_todos_buttons`. Disabled by default. 
  * [Issues, incidents](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/133474), and [epics](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/133881) also updated. 



On self-managed GitLab, by default this feature is not available. To make it available, an administrator can [enable the feature flag](../../../administration/feature_flags.html) named `notifications_todos_buttons`. On GitLab.com and GitLab Dedicated, this feature is not available.

Enabling this feature flag moves the notifications and to-do item buttons to the upper right corner of the page. 

  * On merge requests, these buttons are shown to the far right of the tabs. 
  * On issues, incidents, and epics, these buttons are shown at the top of the right sidebar. 



## Related topics[](#related-topics "Permalink")

  * [Create a merge request](creating_merge_requests.html)
  * [Review a merge request](reviews/index.html)
  * [Authorization for merge requests](authorization_for_merge_requests.html)
  * [Testing and reports](../../../ci/testing/index.html)
  * [GitLab keyboard shortcuts](../../shortcuts.html)
  * [Comments and threads](../../discussions/index.html)
  * [Suggest code changes](reviews/suggestions.html)
  * [CI/CD pipelines](../../../ci/index.html)
  * [Push options](../../../topics/git/commit.html) for merge requests 



## [ Help & feedback  ](#help-feedback-content)

### Docs

[Edit this page](https://gitlab.com/gitlab-org/gitlab/-/blob/master/doc/user/project/merge_requests/index.md) to fix an error or add an improvement in a merge request. [Create an issue](https://gitlab.com/gitlab-org/gitlab/-/issues/new?issue\[description\]=Link%20the%20doc%20and%20describe%20what%20is%20wrong%20with%20it.%0A%0A%3C!--%20Don%27t%20edit%20below%20this%20line%20--%3E%0A%0A%2Flabel%20~documentation%20~%22docs%5C-comments%22%20&issue\[title\]=Docs%20feedback:%20Write%20your%20title) to suggest an improvement to this page. 

### Product

[Create an issue](https://gitlab.com/gitlab-org/gitlab/-/issues/new?issue\[description\]=Describe%20what%20you%20would%20like%20to%20see%20improved.%0A%0A%3C!--%20Don%27t%20edit%20below%20this%20line%20--%3E%0A%0A%2Flabel%20~%22docs%5C-comments%22%20&issue\[title\]=Docs%20-%20product%20feedback:%20Write%20your%20title) if there's something you don't like about this feature. [Propose functionality](https://gitlab.com/gitlab-org/gitlab/-/issues/new?issuable_template=Feature%20proposal%20-%20detailed&issue\[title\]=Docs%20feedback%20-%20feature%20proposal:%20Write%20your%20title) by submitting a feature request. [Join First Look](https://about.gitlab.com/community/gitlab-first-look/) to help shape new features. 

### Feature availability and product trials

[View pricing](https://about.gitlab.com/pricing/) to see all GitLab tiers and features, or to upgrade. [Try GitLab for free](https://about.gitlab.com/free-trial/) with access to all features for 30 days. 

### Get Help

If you didn't find what you were looking for, [search the docs](/search/). 

If you want help with something specific and could use community support, [post on the GitLab forum](https://forum.gitlab.com/new-topic?title=topic%20title&body=topic%20body&tags=docs-feedback). 

For problems setting up or using this feature (depending on your GitLab subscription). 

[Request support](https://about.gitlab.com/support/)

[![Sign in to GitLab.com](/assets/images/gitlab-logo.svg)Sign in to GitLab.com](https://gitlab.com/dashboard)

  * [ Twitter](https://twitter.com/gitlab)
  * [ Facebook ](https://www.facebook.com/gitlab)
  * [ YouTube ](https://www.youtube.com/channel/UCnMGQ8QHMAnVIsI3xJrihhg)
  * [ LinkedIn ](https://www.linkedin.com/company/gitlab-com)



  * [Docs Repo](https://gitlab.com/gitlab-org/gitlab-docs)
  * [About GitLab](https://about.gitlab.com/company/)
  * [Terms](https://about.gitlab.com/terms/)
  * [Privacy Statement](https://about.gitlab.com/privacy/)
  * Cookie Preferences
  * [Contact](https://about.gitlab.com/company/contact/)



View [page source](https://gitlab.com/gitlab-org/gitlab/-/blob/master/doc/user/project/merge_requests/index.md) - Edit in [Web IDE](https://gitlab.com/-/ide/project/gitlab-org/gitlab/edit/master/-/doc/user/project/merge_requests/index.md) [![Creative Commons License](/assets/images/by-sa.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

  * [ Twitter](https://twitter.com/gitlab)
  * [ Facebook ](https://www.facebook.com/gitlab)
  * [ YouTube ](https://www.youtube.com/channel/UCnMGQ8QHMAnVIsI3xJrihhg)
  * [ LinkedIn ](https://www.linkedin.com/company/gitlab-com)



#### [On this page](#)

#### On this page

  * [Create a merge request](#create-a-merge-request)
  * [Use merge request templates](#use-merge-request-templates)
  * [View merge requests](#view-merge-requests)
  * [Filter the list of merge requests](#filter-the-list-of-merge-requests)
  * [By environment or deployment date](#by-environment-or-deployment-date)
  * [Add changes to a merge request](#add-changes-to-a-merge-request)
  * [Assign a user to a merge request](#assign-a-user-to-a-merge-request)
  * [Merge a merge request](#merge-a-merge-request)
  * [Close a merge request](#close-a-merge-request)
  * [Delete the source branch on merge](#delete-the-source-branch-on-merge)
  * [Update merge requests when target branch merges](#update-merge-requests-when-target-branch-merges)
  * [Merge request workflows](#merge-request-workflows)
  * [Filter activity in a merge request](#filter-activity-in-a-merge-request)
  * [Resolve a thread](#resolve-a-thread)
  * [Move all unresolved threads in a merge request to an issue](#move-all-unresolved-threads-in-a-merge-request-to-an-issue)
  * [Move one unresolved thread in a merge request to an issue](#move-one-unresolved-thread-in-a-merge-request-to-an-issue)
  * [Prevent merge unless all threads are resolved](#prevent-merge-unless-all-threads-are-resolved)
  * [Automatically resolve threads in a merge request when they become outdated](#automatically-resolve-threads-in-a-merge-request-when-they-become-outdated)
  * [Move notifications and to-dos](#move-notifications-and-to-dos)
  * [Related topics](#related-topics)



## This website uses cookies

We use cookies to make our websites and services operate correctly, to understand how visitors engage with us and to improve our product and marketing efforts. See our cookie policy for more information.[Cookie Policy](https://about.gitlab.com/privacy/cookies/)

Cookies Settings Accept All Cookies

![Company Logo](https://cdn.cookielaw.org/logos/aa14a5c8-79e3-442a-8177-464ad850b19d/e46c1d0d-1f66-481f-bc06-5427671431da/253e6fee-c4c0-4b60-bc35-79cdae5dda32/gitlab-logo-100.png)

## Privacy Preference Center

  * ### Your Privacy

  * ### Strictly Necessary Cookies

  * ### Functionality Cookies

  * ### Performance and Analytics Cookies

  * ### Targeting and Advertising Cookies




#### Your Privacy

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [Cookie Policy](https://about.gitlab.com/privacy/cookies/)

User ID:  970a5cc2-cf43-46f5-aeaf-8f771a3252f6

This User ID will be used as a unique identifier while storing and accessing your preferences for future.

Timestamp:  --

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, enabling you to securely log into the site, filling in forms, or using the customer checkout. GitLab processes any personal data collected through these cookies on the basis of our legitimate interest.

Cookies Details‎

#### Functionality Cookies

Functionality Cookies

These cookies enable helpful but non-essential website functions that improve your website experience. By recognizing you when you return to our website, they may, for example, allow us to personalize our content for you or remember your preferences. If you do not allow these cookies then some or all of these services may not function properly. GitLab processes any personal data collected through these cookies on the basis of your consent

Cookies Details‎

#### Performance and Analytics Cookies

Performance and Analytics Cookies

These cookies allow us and our third-party service providers to recognize and count the number of visitors on our websites and to see how visitors move around our websites when they are using it. This helps us improve our products and ensures that users can easily find what they need on our websites. These cookies usually generate aggregate statistics that are not associated with an individual. To the extent any personal data is collected through these cookies, GitLab processes that data on the basis of your consent.

Cookies Details‎

#### Targeting and Advertising Cookies

Targeting and Advertising Cookies

These cookies enable different advertising related functions. They may allow us to record information about your visit to our websites, such as pages visited, links followed, and videos viewed so we can make our websites and the advertising displayed on it more relevant to your interests. They may be set through our website by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other websites. GitLab processes any personal data collected through these cookies on the basis of your consent.

Cookies Details‎

Back Button

### Cookie List

Filter Button

Consent Leg.Interest

checkbox label label

checkbox label label

checkbox label label

Clear

checkbox label label

Apply Cancel

Confirm My Choices

Allow All

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=f42c238e7cc8405cf5140390a638e222&_biz_l=https%3A%2F%2Fdocs.gitlab.com%2Fee%2Fuser%2Fproject%2Fmerge_requests%2Findex.html&_biz_t=1733651967928&_biz_i=Merge%20requests%20%7C%20GitLab&_biz_n=0&rnd=298542&cdn_o=a&_biz_z=1733651967929)![](https://cdn.bizibly.com/u?_biz_u=f42c238e7cc8405cf5140390a638e222&_biz_l=https%3A%2F%2Fdocs.gitlab.com%2Fee%2Fuser%2Fproject%2Fmerge_requests%2Findex.html&_biz_t=1733651967933&_biz_i=Merge%20requests%20%7C%20GitLab&rnd=439500&cdn_o=a&_biz_z=1733651967933)
