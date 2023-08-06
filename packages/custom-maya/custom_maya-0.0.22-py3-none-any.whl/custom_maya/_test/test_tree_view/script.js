// 数据
const data = [
    {
        "full_name": "|ROOT"
    },
    {
        "full_name": "|ROOT|WAIST"
    },
    {
        "full_name": "|ROOT|WAIST|SPINE1"
    },
    {
        "full_name": "|ROOT|WAIST|SPINE1|SPINE2"
    },
    {
        "full_name": "|ROOT|WAIST|SPINE1|SPINE2|SPINE3"
    },
    {
        "full_name": "|ROOT|WAIST|SPINE1|SPINE2|SPINE3|SPINE4"
    },
    {
        "full_name": "|ROOT|WAIST|SPINE1|SPINE2|SPINE3|SPINE4|SPINE5"
    },
    {
        "full_name": "|ROOT|WAIST|SPINE1|SPINE2|SPINE3|SPINE4|SPINE5|SPINE6"
    },
    {
        "full_name": "|ROOT|WAIST|THIGH_L"
    },
    {
        "full_name": "|ROOT|WAIST|THIGH_L|CALF_L"
    },
    {
        "full_name": "|ROOT|WAIST|THIGH_L|CALF_L|FOOT_L"
    },
    {
        "full_name": "|ROOT|WAIST|THIGH_L|CALF_L|FOOT_L|TOE_L"
    },
    {
        "full_name": "|ROOT|WAIST|THIGH_R"
    },
    {
        "full_name": "|ROOT|WAIST|THIGH_R|CALF_R"
    },
    {
        "full_name": "|ROOT|WAIST|THIGH_R|CALF_R|FOOT_R"
    },
    {
        "full_name": "|ROOT|WAIST|THIGH_R|CALF_R|FOOT_R|TOE_R"
    },
    {
        "full_name": "|ROOT|WAIST|CLAVICLE_L"
    },
    {
        "full_name": "|ROOT|WAIST|CLAVICLE_L|UPPERARM_L"
    },
    {
        "full_name": "|ROOT|WAIST|CLAVICLE_L|UPPERARM_L|FOREARM_L"
    },
    {
        "full_name": "|ROOT|WAIST|CLAVICLE_L|UPPERARM_L|FOREARM_L|HAND_L"
    },
    {
        "full_name": "|ROOT|WAIST|CLAVICLE_L|UPPERARM_L|FOREARM_L|HAND_L|INDEX_L"
    },
    {
        "full_name": "|ROOT|WAIST|CLAVICLE_L|UPPERARM_L|FOREARM_L|HAND_L|MIDDLE_L"
    },
    {
        "full_name": "|ROOT|WAIST|CLAVICLE_L|UPPERARM_L|FOREARM_L|HAND_L|PINKY_L"
    },
    {
        "full_name": "|ROOT|WAIST|CLAVICLE_L|UPPERARM_L|FOREARM_L|HAND_L|THUMB_L"
    },
    {
        "full_name": "|ROOT|WAIST|CLAVICLE_R"
    },
    {
        "full_name": "|ROOT|WAIST|CLAVICLE_R|UPPERARM_R"
    },
    {
        "full_name": "|ROOT|WAIST|CLAVICLE_R|UPPERARM_R|FOREARM_R"
    },
    {
        "full_name": "|ROOT|WAIST|CLAVICLE_R|UPPERARM_R|FOREARM_R|HAND_R"
    },
    {
        "full_name": "|ROOT|WAIST|CLAVICLE_R|UPPERARM_R|FOREARM_R|HAND_R|INDEX_R"
    }
];


function func_t() {
    console.log('func_t');
};


function createTree(data) {
    console.log('executing creatTree');
    const tree = document.getElementById('outline-tree');

    function createNode(name, depth) {
        const li = document.createElement('li');
        li.dataset.depth = depth;

        const toggleButton = document.createElement('button');
        toggleButton.classList.add('toggle-icon', 'btn', 'btn-sm', 'btn-outline-primary');
        toggleButton.type = 'button';
        li.appendChild(toggleButton);

        const textNode = document.createElement('button');
        textNode.textContent = name;
        textNode.type = 'button';
        textNode.classList.add('node-name-btn', 'btn', 'btn-sm', 'btn-outline-secondary');
        li.appendChild(textNode);

        toggleButton.addEventListener('click', function (event) {
            event.stopPropagation();

            const ul = li.querySelector('ul');
            if (ul) {
                const expand = ul.style.display === 'none';
                ul.style.display = expand ? 'block' : 'none';
                toggleButton.classList.toggle('plus');
                toggleButton.classList.toggle('minus');
                if (event.shiftKey) {
                    toggleAll(li, expand);
                }
            }
        });

        // 添加防御代码
        const ul = li.querySelector('ul');
        if (ul && ul.children.length > 0) {
            toggleButton.classList.add('plus');
        }

        return li;
    }


// 递归切换所有子节点
    function toggleAll(node, expand) {
        const ul = node.querySelector('ul');
        const toggleIcon = node.querySelector('.toggle-icon');
        if (ul && ul.children.length > 0 && toggleIcon) { // 添加防御代码
            ul.style.display = expand ? 'block' : 'none';
            toggleIcon.classList.toggle('plus', !expand);
            toggleIcon.classList.toggle('minus', expand);
            Array.from(ul.children).forEach((child) => toggleAll(child, expand));
        }
    }


    data.forEach((item) => {
        const names = item.full_name.split('|').filter((name) => name !== '');
        let parentNode = tree;

        names.forEach((name, index) => {
            let node = parentNode.querySelector(`li[data-name="${name}"]`);
            if (!node) {
                const hasChildren = index < names.length - 1;
                node = createNode(name, index, hasChildren);
                node.dataset.name = name;

                const ul = document.createElement('ul');
                ul.style.display = 'none';
                node.appendChild(ul);

                parentNode.appendChild(node);
            }
            parentNode = node.querySelector('ul');
        });
    });


    // 为有子节点的节点添加切换图标
    document.querySelectorAll('#outline-tree li').forEach(function (element) {
        const ul = element.querySelector('ul');
        if (ul.children.length > 0) {
            const toggleIcon = element.querySelector('.toggle-icon');
            toggleIcon.classList.add('plus');
            ul.style.paddingLeft = '20px'; // 修改这里，添加偏移
        } else {
            ul.remove();
        }
    });
};

createTree(data);